import argparse
from PIL import Image


def load_image():
    image = Image.open("scan.jpg")
    return image


def resize_image(path_to_original, path_to_result):
    pass


if __name__ == '__main__':
    load_image()
