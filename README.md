Pyard Bone Scripts
------------------

### Data ingest solution for [Boneyard.io](http://boneyard.io)

### [Presentation](https://docs.google.com/presentation/d/180hNyxObl0PP7tZU3B3jl8ClTXZkziY7YOfmmdX-dh8/edit?usp=sharing)



A list of scripts for cleaning up the data for the Bone Explorer
data.

* `stlremesh.py` Uses meshlab server to filter stls
* `clean_data.py` Will pull nested directories into a flat/consistent structure
* `scrape_pca` Will return desired values form PCA in dict
* `extract_metadata` Will return all the metadata extracted from plain text
* `sketchfab_upload` Will upload STL to sketchfab and return URL info

Dependencies:

* catdoc
* imagemagick
* requests
* meshlab server
* python-3.X

TODO

- [x] STL upload script

- [x] catdoc 
 


