try: 
    from wand.image import Image
    from wand.color import Color
except ModuleNotFoundError: print("Please run \"pip install cairosvg\"")
from sys import argv as a

if a.count == 1:
    print("FileName, Height, Width, OutputFile required im arguments!")

original = a[1]
height   = int(a[2])
width    = int(a[3])
output   = a[4]

with Image(filename=original, width=width, height=height, background=Color('transparent')) as image:
    open(output, mode='wb').write(image.make_blob('png'))