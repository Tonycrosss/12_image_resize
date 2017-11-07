import argparse
from PIL import Image
import os


def load_image(path_to_image):
    image = Image.open(path_to_image)
    return image


def resize_image(image, width, height, scale):
    old_image_width = image.size[0]
    old_image_height = image.size[1]
    if width is None and height is not None:
        width = height * old_image_width // old_image_height
    if height is None and width is not None:
        height = width * old_image_height // old_image_width
    if width is None and height is None and scale is not None:
        resized_image = image.resize((int(old_image_width * scale),
                                      int(old_image_height * scale)))
    elif scale is not None and (width is not None or height is not None):
        raise Exception('Error, u cannot use scale and width/height together!')
    else:
        resized_image = image.resize((width, height))
    return resized_image


def save_image(image, dirpath):
    width = image.size[0]
    height = image.size[1]
    image.save(dirpath + 'pic__{}x{}.jpg'.format(width, height))


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--img', type=str, help='Enter path to image',
                        required=True)
    parser.add_argument('--width', type=int, const=None,
                        help='Enter new width')
    parser.add_argument('--height', type=int, const=None,
                        help='Enter new heigh')
    parser.add_argument('--scale', type=float, const=None,
                        help='Enter scale')
    parser.add_argument('--out', type=str, help='Enter new_file_path')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    path_to_image = args.img
    new_width = args.width
    new_height = args.height
    scale = args.scale
    if args.out == None:
        new_image_path = os.path.dirname(args.img) + '\\'
    else:
        new_image_path = args.out
    image = load_image(path_to_image)
    resized_image = resize_image(image, new_width, new_height, scale)
    save_image(resized_image, new_image_path)

