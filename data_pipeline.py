from sys import argv
from clean_data import walk_and_clean
from extract_metadata import get_all_metadata

_, root_dir = argv

walk_and_clean(root_dir)
get_all_metadata(root_dir)



