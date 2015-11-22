import os

from json import dumps
from uuid import uuid4
from shutil import copy2
from sys import argv
from time import time
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
    return f.endswith('tif') or f.endswith('tiff') or f.endswith('stl') or f.endswith('pca')

def is_tiff_stack(path):
    files = [file for file in os.listdir(path)]
    exts = [os.path.splitext(f)[1] for f in files]
    return all([ext.lower()=='.tiff' or ext.lower()=='.tif' for ext in exts])

def status(root, **kwargs):
    filepath = os.path.join(root, 'status.txt')
    with open(filepath, 'w') as f:
        f.write(dumps(kwargs))

def walk_and_clean(walking_root):
    '''returns dict of relevant media paths'''
    ROOT = str(uuid4())
    files_written = 0
    new_root = os.path.join(walking_root, ROOT)
    os.mkdir(new_root)

    status(new_root,
        timestamp=int(time()),
        state='initializing',
        files_written=files_written
    )

    walkable = os.walk(walking_root)
    root_depth = len(root.split('/'))
    for dir_path, dir_names, filenames in walkable:
        if ROOT in dir_path:
            continue

        movable_files = [
            filename for filename in filenames if is_eligable_file(filename)
        ]

        if not movable_files:
            continue

        specimen_name = dir_path.split('/')[root_depth]
        specimen_path = os.path.join(new_root, specimen_name)
        make_unless_exists(specimen_path)

        if all([filename.lower().endswith('stl') or filename.lower().endswith('pca') for filename in movable_files]):
            curr_dir = 'extra_data'
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
            files_written += 1
            status(new_root,
                timestamp=int(time()),
                state='processing',
                files_written=files_written
            )

    status(new_root,
        timestamp=int(time()),
        state='finished',
        files_written=files_written
    )

def find_tiff_stacks(root_dir):
    tiff_stacks = {}
    for dir_path, dir_names, filenames in os.walk(root_dir):
        print(dir_path)
        if is_tiff_stack(dir_path):
            print('current dir {} is a tiff stack'.format(dir_path))
            file_list = [os.path.join(dir_path, file) \
                         for file in filenames] 
            tiff_stacks[os.path.basename(dir_path)] = file_list 
    return tiff_stacks

if __name__ == '__main__':
    _, root = argv
    walk_and_clean(root)
    print(find_tiff_stacks(root))

