
# note for mac: pip install Pillow to get PIL
import PIL
from PIL import Image
import argparse
import os

ios_sizes = {
    'iphone4': (640, 960),
    'iphone5': (640, 1136),
    'iphone6': (750, 1334),
    'iphone6plus': (1242, 2208),
}

def generate_image(image, phone, size):
    im = Image.open(image)
    name = image.split(".")[-2].split("/")[-1]
    path = os.path.dirname(image)
    old_width, old_height = im.size
    new_width, new_height = size
    resize_height = int(old_height * new_width / float(old_width))
    
    im = im.resize((new_width, resize_height), Image.ANTIALIAS)
    im = im.crop((0, 0, new_width, new_height))
    im.save("%s/%s-%s.png" % (path, name, phone), "PNG")
    
def generate_all_images(image):
    im = Image.open(image)
    if im.size != (1242, 2208):
        print("Your image must start as 1242x2208")
        return

    for phone, size in ios_sizes.iteritems():
        generate_image(image, phone, size)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert an image to App Store screenshots.')
    parser.add_argument('-i', metavar="image", dest="image", help='the input image.', required=True)
    args = parser.parse_args()
    generate_all_images(args.image)
