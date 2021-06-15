from PIL import Image
import glob
import os

# directory of image(s) to convert
from_path = 'originals/'

# Resulting png size
size = (100, 100)

# palette for yellow inky display (black base color)
y_palette = [0, 0, 0,  # Black
             255, 255, 255,  # White
             255, 255, 0,  # Yellow
             255, 255, 255]  # White

# palette for red inky display (black base color)
r_palette = [0, 0, 0,  # Black
             255, 255, 255,  # White
             255, 0, 0,  # Red
             255, 255, 255]  # White

# directory to store image(s)
to_path = 'icons/'


def inky_image_converter(from_path, size, palette, to_path):
    '''
    This function takes local images and converts them to a smaller size using a defined palette.
    :params from_path: path to image directory
    :params size: 2 touple indicating height x width in pixels.
    :params palette: palette to be used
    :params to_path: path of directory to store converted .pngs 
    '''

    # loop through files in from_path directory
    for infile in glob.glob(f'{from_path}*.png'):
        # seperate ext from file path/name
        root, ext = os.path.splitext(infile)
        # seperate name from path
        file = os.path.basename(root)
        # open image to convert
        with Image.open(infile) as im:
            # create icon from converted image
            icon = im.convert('P', dither=Image.NONE)
            # apply colour palette
            icon.putpalette(palette)
            # size down
            icon.thumbnail(size)
            # save to provided path using original name
            icon.save(
                to_path + file+'.png', 'PNG')
            # print file name and path
            print(f'Saved {file}.png to {to_path}')


inky_image_converter(from_path, size, y_palette, to_path)
