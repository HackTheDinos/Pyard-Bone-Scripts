import os

from uuid import uuid4
from shutil import copy2
from sys import argv

# takes argument of the root dir of the data:
# IE: python clean_data.py /Users/deansilfen/HTD/CTdata_copy
# takes around 10 seconds to run on ~15GB of data

def make_unless_exists(path):
    if not os.path.exists(path):
        os.mkdir(path)
        return True
    return False

def is_eligable_file(f):
    f = f.lower()
    return f.endswith('tif') or f.endswith('tiff') or f.endswith('stl')

def walk_and_clean(walking_root):
    walkable = os.walk(root)
    ROOT = str(uuid4())
    new_root = os.path.join(root, ROOT)
    os.mkdir(new_root)
    root_depth = len(root.split('/'))

    for dir_path, dir_names, filenames in walkable:
        if dir_path.endswith(ROOT + '/'):
            continue

        movable_files = [
            filename for filename in filenames if is_eligable_file(filename)
        ]

        if not movable_files:
            continue

        specimen_name = dir_path.split('/')[root_depth]
        specimen_path = os.path.join(new_root, specimen_name)
        make_unless_exists(specimen_path)

        if all([filename.lower().endswith('stl') for filename in movable_files]):
            curr_dir = 'STL_data'
        else:
            curr_dir = os.path.dirname(dir_path).split('/')[-1]

        new_path = os.path.join(specimen_path, curr_dir)
        existing_path =  make_unless_exists(new_path)

        if not existing_path:
            new_path = os.path.join(specimen_path, str(uuid4()) + curr_dir)
            make_unless_exists(new_path)

        for files in movable_files:
            old_files_path = os.path.join(dir_path, files)
            new_files_path = os.path.join(new_path, files)
            copy2(old_files_path, new_files_path)


if __name__ == '__main__':
    _, root = argv
    walk_and_clean(root)

