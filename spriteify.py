import sys,os
#import piexif
#from PIL import Image

# walk through each directory of files,
# if there are more than 50 files,
# find out how many files should

def new_name(old_name):
    old_name = old_name.split('.')[0]
    return  + old_name + '.png'

def clean_tiff(tiff):
   # exif_dict = piexif.load(tiff)

    #if exif_dict.get('0th'):
     #   exif_dict['ImageDescription'] = 'This is not null'
      #  new_tiff = Image.open(tiff)
       # tiff = 'temp.tiff'
        #new_tiff.save(tiff, exif=e)

    call('convert {0} -size 320x240 {1}'.format(tiff, new_name(tiff)))


