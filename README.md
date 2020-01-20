# Requirements

```

Python 3.6+

```

# Purpose

Given an OpenRaster Image (.ora) file with a specific layer arrangement, this script generates an HTML file that contains your art and a color picker that allows the user to change the color of a selected region of the art. Useful for when you might be drawing something for someone and you do not know what the base colors should be, so you can send them the generated HTML file which they can open in Google Chrome to play around with different colors.

#### // TODO add gif demoing generated html

# How to use

You will need to export your Krita document (.kra) as an OpenRaster Image (.ora) containing:

- a group layer named "outline", which includes paint layers for your line art; you do not need to give these layers meaningful names; merging all these layers is more ideal, but the script will function without merging.

- a group layer named "color", which includes paint layers for individual sections of the drawing (for example, a layer for a shirt, and a separate layer for pants); give these layers meaningful names; these can all be one color.

#### // TODO add image

When you have the .ora file that satisfies the above conditions, you can run the python script in the console:

```bash
python3 main.py path/to/openraster/image.ora
```

This will print the contents of the HTML file to stdout; so instead you can redirect the output to a file

```bash
python3 main.py path/to/openraster/image.ora > path/to/file.html
```
