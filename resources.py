from urllib.request import urlopen

def readlinesToOneLine(obj):
    return ''.join([line.decode('utf-8').strip() for line in obj.readlines()])

def getColorSelectorScript():
    js = r'https://raw.githubusercontent.com/TysonNgo/HTML-Color-Selector/master/index.js'

    with urlopen(js) as conn:
        return '<script type="text/javascript">' + \
        readlinesToOneLine(conn) + \
        '</script>'

def getColorSelectorStyle():
    css = r'https://raw.githubusercontent.com/TysonNgo/HTML-Color-Selector/master/index.css'

    with urlopen(css) as conn:
        return '<style type="text/css">' + \
        ''.join([line.decode('utf-8').strip() for line in conn.readlines()]) + \
        '</style>'

def getMainScript():
    with open('index.js', 'rb') as f:
        return '<script type="text/javascript">' + \
        readlinesToOneLine(f) + \
        '</script>'

def getMainHelperScript(ids):
    """ ids - [(id, name, ...)]
    """
    ids = [i[0] for i in ids]

    return '<script type="text/javascript">' + \
    'let hsv_values = {'                     + \
        ','.join(
            [f'"{i}": {{ h:0, s:0, v:50 }}'
            for i in ids])                   + \
    '};'                                     + \
    f'let key = "{ids[-1]}";' + \
    '</script>'

def getMainStyle():
    with open('index.css', 'rb') as f:
        return '<style type="text/css">' + \
        readlinesToOneLine(f) + \
        '</style>'

def getHTMLTemplate():
    with open('template') as f:
        return f.readlines()