import sys,os
#import piexif
#from PIL import Image
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
### GETTING THE DATA
def process_files(dir_path, filenames):
    total_files = len(filenames)
    if total_files <= MAX_FILE_COUNT:
        return filenames

    step = ceil(total_files / MAX_FILE_COUNT)
    chosen_files = filenames[::step]
    for filename in chosen_files:
        shrink_tiff(dir_path, filename)
    return chosen_files

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

