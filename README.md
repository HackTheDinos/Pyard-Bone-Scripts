Pyard Bone Scripts
------------------

### Data ingest solution for [Boneyard.io](http://boneyard.io)

### [Presentation](https://docs.google.com/presentation/d/180hNyxObl0PP7tZU3B3jl8ClTXZkziY7YOfmmdX-dh8/edit?usp=sharing)

### What we accomplished

#### Scraping metadata from specimen directory
  * Pulled from PCA:
    * geometry_voxel_y
    * geometry_voxel_x
    * xray_voltage
    * xray_current
    * ct_number_images
    * calib_averaging
    * calib_num_image
    * calib_skip
    * detector_timing_value
    * institutional_id
  * From .DOC files:
    * all unstructured text:
      * could include Species, location found, etc.

### File cleaning and management
  * Directory structure is standardized
  * Pushed to large file sorage
  * Keep URI (location) of ingested files

### Create proxy assets for website
  * Create 2D sprite-sheet
  * Create interactive 3D model

#### What we would do next
  * Connect the dots
  * Scale up ingest servers
  * Settle on Data standards and practices with institutions

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

- [] setup ingest API 
- [] setup ingest server



