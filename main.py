import sys
import zipfile
import xml.etree.ElementTree as ET
from base64 import b64encode
from resources import *

def print_requirements():
    pass

def stack_XML_to_dict(xml):
    image = ET.fromstring(xml)
    root = image.find('.//stack[@name="root"]')
    outlines = []
    colors = []

    stack = [root]
    while stack:
        elem = stack.pop()
        name = elem.attrib['name'].strip().lower()
        
        if name == 'outline':
            outlines.append(elem)
            continue
        elif name == 'color':
            colors.append(elem)
            continue

        stack.extend(list(elem))

    outline_layers = []
    color_layers = []

    for outline in outlines[::-1]:
        outline_layers.extend([e for e in outline.iter() if e.tag == 'layer'])

    for color in colors[::-1]:
        color_layers.extend([e for e in color.iter() if e.tag == 'layer'])


    viewbox_w, viewbox_h = image.attrib['w'], image.attrib['h']
    return {
        'w': viewbox_w,
        'h': viewbox_h,
        'outlines': [l.attrib for l in outline_layers],
        'colors': [l.attrib for l in color_layers]
    }

def print_SVG_and_get_color_IDs(ora):
    with zipfile.ZipFile(ora) as z:
        xml = z.read('stack.xml')
        x = stack_XML_to_dict(xml)
        ids = [(id(color), color['name']) for color in x['colors']]

        # print svg ----------------------------------------------------------------------------------------------

        print (f'<svg viewBox="0 0 {x["w"]} {x["h"]}" >')

        for color, id_name in zip(x['colors'], ids):
            ID, _ = id_name
            print (f'<filter id="colorMatrix{ID}" color-interpolation-filters="sRGB">')
            print (f'<feColorMatrix in="SourceGraphic" type="matrix" ')
            print ('values="')
            print ('0 0 0 0 0.5 '*3)
            print ('0 0 0 1 0" />')
            print ('</filter>')

        for color, id_name in zip(x['colors'], ids):
            ID, _ = id_name
            b64_png = b64encode(z.read(color["src"])).decode("utf-8")
            print ( f'<image filter="url(#colorMatrix{ID})" href="data:image/png;base64,{b64_png}" />' )

        for outline in x['outlines']:
            b64_png = b64encode(z.read(outline["src"])).decode("utf-8")
            print ( f'<image href="data:image/png;base64,{b64_png}" />' )

        print (f'</svg>')

        # --------------------------------------------------------------------------------------------------------

    return ids

def print_buttons(ids):
    """ids - [(int, str), ...]
    """
    for ID,name in ids:
        print (f'<button id="button{ID}">')
        print (name)
        print ('</button>')

def main():
    if not sys.argv[1].endswith('.ora'):
        print_requirements()
        sys.exit(1)
    
    ora = sys.argv[1]
    template = getHTMLTemplate()

    ids = []

    for line in template:
        line = line.strip()
        if line == '$$STYLE_HERE$$':
            print ( getColorSelectorStyle() )
            print ( getMainStyle() )
        elif line == '$$SVG_HERE$$':
            ids[:] = print_SVG_and_get_color_IDs(ora)
        elif line == '$$BUTTONS_HERE$$':
            print_buttons(ids)
        elif line == '$$SCRIPTS_HERE$$':
            print ( getColorSelectorScript() )
            print ( getMainHelperScript(ids) )
            print ( getMainScript() )
        else:
            print (line)


if __name__ == '__main__':
    main()