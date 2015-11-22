'''
    * Pull these items for transaction
      "geometry_voxel_y"
      "geometry_voxel_x"
      "xray_voltage"
      "xray_current"
      "ct_number_images"
      "calib_averaging"
      "calib_num_image"
      "calib_skip"

    return dict?
'''

import configparser

def get_pca_dict(pca_path):
    cp = configparser.ConfigParser()
    cp.read(pca_path)

    pca_dict = {
        "geometry_voxel_x": cp.get('Geometry','VoxelSizeX'),
        "geometry_voxel_y": cp.get('Geometry','VoxelSizeY'),
        "xray_voltage": cp.get('Xray','Voltage'),
        "xray_current": cp.get('Xray', 'Current'),
        "ct_number_images": cp.get('CT','NumberImages'),
        "calib_averaging": cp.get('CalibValue', 'Averaging'),
        "calib_num_image": cp.get('CalibValue', 'NumberImages'),
        "calib_skip": cp.get('CalibValue', 'Skip'),
        "detector_timing_value": cp.get('Detector', 'TimingVal'),

    }
    return pca_dict

if __name__ == '__main__':
     from sys import argv  
     _, pca_path = argv
     print(get_pca_dict(pca_path))




