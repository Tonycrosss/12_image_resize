import argparse
from PIL import Image


def load_image():
    image = Image.open("scan.jpg")
    return image


def resize_image(image, width=None, height=None, scale=None, path_to_result='./__pic.jpg'):
    old_image_width = image.size[0]
    old_image_height = image.size[1]
    if width == None and height != None:
        size_difference = abs(height - old_image_height)
        width = old_image_width - size_difference
    if height == None and width != None:
        size_difference = abs(width - old_image_width)
        height = old_image_height - size_difference
    if scale != None:
        resized_image = image.resize((width * scale, height * scale))
    else:
        resized_image = image.resize((width, height))
    return resized_image


def save_image(image, filepath='./'):
    pass



if __name__ == '__main__':
    image = load_image()
    resized_image = resize_image(image, width=300, height=300)
    save_image(resized_image)
