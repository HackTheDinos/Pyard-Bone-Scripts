import os
from math import ceil
from sys import argv
from uuid import uuid4

import piexif
from PIL import Image

MAX_FILE_COUNT = 50

### PROCESSING THE DATA
def new_name(old_name):
    old_name = old_name.split('.')[0]
    return 'tmp_sprite_' + old_name + '.png'

def clean_tiff(path, tiff):
    new_tiff_path = os.path.join(path, tiff)
    try:
        exif_dict = piexif.load(new_tiff_path)
        if not exif_dict.get('ImageDescription'):
            exif_dict['ImageDescription'] = 'This is not null'
    except ValueError:
        print('File {} is borked'.format(new_tiff_path))
        exif_dict = {} # TODO: generate exif data? I guess?
        return

    new_tiff = Image.open(new_tiff_path)
    new_tiff.save(new_tiff_path, exif=exif_dict)
    new_png_name = new_name(tiff)
    new_png_path = os.path.join(path, new_png_name)
    call('convert {0} --type Grayscale {1}'.format(new_tiff_path, new_png_path))
    return new_png_path

### GETTING THE DATA
def process_files(dir_path, filenames):
    total_files = len(filenames)
    if total_files <= MAX_FILE_COUNT:
        return filenames

    step = ceil(total_files / MAX_FILE_COUNT)
    chosen_files = filenames[::step]
    try:
        test_path = os.path.join(dir_path, chosen_files[0])
        test_img = Image.open(test_path)
    except IndexError:
        return False

    width = test_img.width * len(chosen_files)
    height = test_img.height
    blank_image = Image.new("RGB", (width, height))
    paste_cords = (0, 0) # X, Y

    for filename in chosen_files:
        png_path = clean_tiff(dir_path, filename)
        if not png_path:
            continue
        png = Image.open(png_path)
        blank_image.paste(png, paste_cords)
        x, y = paste_cords
        paste_cords = ((test_img.width + x), y)

    sprite_path = os.path.join(dir_path, 'sprite_sheet.png')
    blank_image.save(sprite_path)
    return sprite_path

def walk_tiffs(root):
    walkable = os.walk(root)
    for dir_path, dir_names, filenames in walkable:
        tiff_files = [
            filename for filename in filenames if filename.lower().endswith('tif') or filename.lower().endswith('tiff')
        ]
        if not tiff_files:
            continue

        files = process_files(dir_path, tiff_files)
        print(files)


if __name__ == '__main__':
    _, root = argv
    walk_tiffs(root)

