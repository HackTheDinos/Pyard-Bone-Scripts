from uuid import uuid4
import piexif
from PIL import Image

# walk through each directory of files,
# if there are more than 50 files,
# find out how many files should

def new_name(old_name):
    old_name = old_name.split('.')[0]
    return 'new_' + old_name + '.png'

def get_tiffs(path, filenames):
    for filename in filenames:
        clean_tiff(path, filename)
        

def clean_tiff(path, tiff):
    exif_dict = piexif.load(tiff)
    exif_dict['ImageDescription'] = 'This is not null'
    new_tiff = Image.open(tiff)
    tiff = str(uuid4()) + '_temp.tiff'
    new_tiff.save(tiff, exif=e)
    call('convert {0} --type Grayscale {1}'.format(tiff, new_name(tiff)))


