import argparse
from PIL import Image


def load_image():
    image = Image.open("scan.jpg")
    return image


def resize_image(image, width=None, height=None, scale=None, path_to_result='./__pic.jpg'):
    old_image_width = image.size[0]
    old_image_height = image.size[1]
    if width == None and height != None:
        width = height * old_image_width // old_image_height
    if height == None and width != None:
        height = width * old_image_height // old_image_width
    if width == None and height == None and scale != None:
        resized_image = image.resize((int(old_image_width * scale), int(old_image_height * scale)))
    elif scale != None and (width != None or height != None):
        raise 'Error'
    else:
        resized_image = image.resize((width, height))
    return resized_image


def save_image(image, filepath='./'):
    image.save(filepath + 'piccccc.jpg')


if __name__ == '__main__':
    image = load_image()
    resized_image = resize_image(image)
    save_image(resized_image)
