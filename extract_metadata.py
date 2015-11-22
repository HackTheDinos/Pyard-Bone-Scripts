import os

import requests

from scrape_pca import get_pca_dict
import extract_doc

ENDPOINT = 'http://boneyard.io/api/specimens'

# walk and find ID and PCA
def find_first_ext_match(ext, root_dir):
    '''
    find first PCA we come across
    '''
    for root, dirs, files in os.walk(root_dir):
        for filename in files:
            if os.path.splitext(filename)[1].lower() == ext.lower():
                return os.path.join(root, filename)

def find_filename(name, path):
    for root, dirs, files in os.walk(path):
        if name.lower() in (filename.lower() for filename in files):
            return os.path.join(root, name)

def get_all_metadata(root_dir):
    '''
    tries to scrape metadata from:
        * PCA file
        * ID.txt
    '''
    id_file = find_filename('id.txt', root_dir)
    if id_file:
        id= open(id_file).read().strip()
    else:
        id= 'None found'
    all_data = {'institutional_id':id}
    pca_file = find_first_ext_match('.pca', root_dir)
    pca_data = get_pca_dict(pca_file)

    if pca_data:
        all_data.update(pca_data)

    xdoc = extract_doc.walk(root_dir)
    if xdoc:
        all_data.update(xdoc)

    resp = requests.post(ENDPOINT, data=all_data)
    return all_data

if __name__ == "__main__":
    from sys import argv
    if len(argv) > 1:
        _,root_dir = argv
    else:
        root_dir = '.'
    print(get_all_metadata(root_dir))




