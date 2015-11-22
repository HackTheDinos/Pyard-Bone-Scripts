import os
from sys import argv

MAX_FILE_COUNT = 50

def determine_files(filenames):
    total_files = len(tiff_files)
    if total_files <= MAX_FILE_COUNT:
        return filenames


    # take an array of filenames, return a new array of ones that need processing

def walk_tiffs(root):
    walkable = os.path.walk(root)
    for dir_path, dir_names, filenames in walkable:
        tiff_files = [
            filename for filename in filenames if filename.lower().endswith('tiff') or filename.lower().endswith('tiff')
        ]

        if not tiff_files:
            continue

        files = determine_files(tiff_files)



if __name__ == '__main__':
    _, root = argv

