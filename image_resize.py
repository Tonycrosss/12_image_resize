import argparse
from PIL import Image


def load_image(path_to_image):
    image = Image.open(path_to_image)
    return image


def resize_image(image, width=None, height=None, scale=None):
    old_image_width = image.size[0]
    old_image_height = image.size[1]
    if width == None and height != None:
        width = height * old_image_width / old_image_height
    if height == None and width != None:
        height = width * old_image_height / old_image_width
    if width == None and height == None and scale != None:
        resized_image = image.resize((int(old_image_width * scale),
                                      int(old_image_height * scale)))
    elif scale != None and (width != None or height != None):
        raise 'Error'
    else:
        resized_image = image.resize((width, height))
    return resized_image


def save_image(image, filepath):
    width = image.size[0]
    height = image.size[1]
    image.save(filepath + 'pic__{}x{}.jpg'.format(width, height))


def parsing_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--img', type=str, nargs=1, help='Enter path to image',
                        required=True)
    parser.add_argument('--width', type=int, nargs=1, const=None,
                        help='Enter new width')
    parser.add_argument('--height', type=int, nargs=1, const=None,
                        help='Enter new heigh')
    parser.add_argument('--scale', type=int, nargs=1, const=None,
                        help='Enter scale')
    parser.add_argument('--out', type=str, nargs=1, const='./',
                        help='Enter new_file_path')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parsing_args()
    path_to_image = args.img
    new_width = args.width
    new_height = args.height
    scale = args.scale
    new_image_path = args.out
    image = load_image(path_to_image)
    resized_image = resize_image(image, new_width, new_height, scale)
    save_image(resized_image, new_image_path)

