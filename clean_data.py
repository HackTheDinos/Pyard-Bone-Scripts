import os

from uuid import uuid4
from shutil import copy2
from sys import argv


def make_unless_exists(path):
    if not os.path.exists(path):
        os.mkdir(path)
        return True
    return False

def walk_and_clean(walking_root):
    walkable = os.walk(root)
    ROOT = str(uuid4())
    new_root = os.path.join(root, ROOT)
    os.mkdir(new_root)
    root_depth = len(root.split('/'))

    for dir_path, dir_names, filenames in walkable:
        if dir_path.endswith(ROOT + '/'):
            continue

        tiff_files = [
            tiff for tiff in filenames if tiff.lower().endswith('tif') or tiff.lower().endswith('tiff')
        ]

        if not tiff_files:
            continue

        specimen_name = dir_path.split('/')[root_depth]

        specimen_path = os.path.join(new_root, specimen_name)
        make_unless_exists(specimen_path)

        curr_dir = os.path.dirname(dir_path).split('/')[-1]
        new_path = os.path.join(specimen_path, curr_dir)
        existing_path =  make_unless_exists(new_path)

        if not existing_path:
            new_path = os.path.join(specimen_path, str(uuid4()) + curr_dir)
            make_unless_exists(new_path)

        for tiff in tiff_files:
            old_tiff_path = os.path.join(dir_path, tiff)
            new_tiff_path = os.path.join(new_path, tiff)
            copy2(old_tiff_path, new_tiff_path)

if __name__ == '__main__':
    _, root = argv
    walk_and_clean(root)

