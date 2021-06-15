This program processes .png files and allows them to be used on an Pimoroni Inky pHat/wHat display.
found here: https://shop.pimoroni.com/products/inky-phat?variant=12549254905939.

It uses the PIL library and converts all images in the provied directory to a new image using a 3 color palette as well as shrinking them to a specified size.

Example:

![Original image](https://github.com/MattSharp0/InkyImager/blob/main/originals/38.png)

![Converted image](https://github.com/MattSharp0/InkyImager/blob/main/icons/38.png)

The fuction takes 4 parameters:

1. from_path (directory of images you wish to convert)
2. size (2 touple; (width, height) in pixels) \* Note: size must be smaller than original image
3. palette (list of ints)
4. to_path (directory to save converted images)
