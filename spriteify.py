import sys,os
#import piexif
#from PIL import Image
import os
import gc

from math import ceil
from subprocess import call
from sys import argv
from uuid import uuid4

from PIL import Image

MAX_FILE_COUNT = 50

### PROCESSING THE DATA
def new_name(old_name):
    old_name = old_name.split('.')[0]
    return 'tmp_sprite_' + old_name + '.png'

def clean_tiff(path, tiff):
    print('PATH ' + path)
    print('FILE ' + tiff)
    tiff_path = os.path.join(path, tiff)
    new_png_name = new_name(tiff)
    new_png_path = os.path.join(path, new_png_name)
    call('convert {0} -resize 640x480 -gravity center -background white -extent 640x480 {1}'.format(tiff_path, new_png_path), shell=True)
    return new_png_path

### GETTING THE DATA
def process_files(dir_path, filenames):
    total_files = len(filenames)
    if total_files <= MAX_FILE_COUNT:
        return filenames

    step = ceil(total_files / MAX_FILE_COUNT)
    chosen_files = filenames[::step]
    width = 640 * len(chosen_files)
    height = 480
    blank_image = Image.new("RGB", (width, height))
    paste_cords = (0, 0) # X, Y

    processed_files = 0
    for filename in chosen_files:
        print(filename)
        print(dir_path)
        p = os.path.join(dir_path, filename)
        try:
            print("TIFF_PATH_EXISTS:{} ".format(os.path.exists(p)))
            png_path = clean_tiff(dir_path, filename)
        except:
            print("{} filename broke".format(filename))
            png_path = None
        if not png_path:
            continue
        png = Image.open(png_path)
        blank_image.paste(png, paste_cords)
        x, y = paste_cords
        paste_cords = ((640 + x), y)
        processed_files += 1

    print(processed_files)
    sprite_path = os.path.join(dir_path, 'sprite_sheet.png')
    if processed_files:
        blank_image.save(sprite_path)
    return sprite_path

def walk_tiffs(root):
    walkable = os.walk(root)
    for dir_path, dir_names, filenames in walkable:
        if 'sprite_sheet.png' in filenames:
            continue

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

