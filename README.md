Pyard Bone Scripts
------------------

A list of scripts for cleaning up the data for the Bone Explorer
data.

* `stlremesh.py` Uses meshlab server to filter stls
* `clean_data.py` Will pull nested directories into a flat/consistent structure
* `scrape_pca` Will return desired values form PCA in dict
* `extract_metadata` Will return all the metadata extracted from plain text
* `sketchfab_upload` Will upload STL to sketchfab and return URL info

Dependencies:

* catdoc
* ffmpeg
* imagemagick
* meshlab server
* python-3.X

TODO

- [] STL upload script

  - [] find out why polling requests on sketchfab_upload doesn't update

- [x] catdoc 
 
- [x] WHY THE HECK CLEAN_DATA CAN'T POINT TO EXT PATH????


