#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Script to use the mxl scripts from meshlabserver
to apply filters to the meshes, to compress file
size.

Usage:
    python3 stlremesh.py <input filename> <output filename>
"""

import argparse
import subprocess
import os.path
import sys

THRESHOLD = 5 

def remesh(i, o):
    script_location = os.path.realpath(__file__)
    script_location = os.path.split(script_location)[0]
    mlx_script = os.path.join(script_location, 'quad.mlx')
    #Quad.mlx uses quad Edge Collapse Decimation
    s = subprocess.call(['meshlabserver', '-i', i, '-o', o, '-s',
                        mlx_script,], stdout = subprocess.DEVNULL,
                        stderr = subprocess.DEVNULL)
    print("Completed file {}".format(o))

def size_of_file(f, o):
                  # Bytes     Kils Megs
    size = os.path.getsize(f)//1024//1024
    print(f,size)

    if size <= 5:
        # Copy file to output

        # shutile warning: shutil copy[2]() can't copy
        # all file metadata.  We'll use subprocess again
        # since this will be working on a Linux Server anyway

        s = subprocess.call(['cp', f, o], stdout = subprocess.DEVNULL,
                stderr = subprocess.DEVNULL)


        print("File {} is less than the threshold {}, copying"
        " to {}".format(f, THRESHOLD, o))

        sys.exit()

    remesh(f, o)

def parser_cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Input File')
    parser.add_argument('output', help='Output File')
    p = parser.parse_args()
    return p.input, p.output

def main():
    i, o = parser_cli()
    print("Applying remesh to {}".format(i))
    size_of_file(i, o)
    #remesh(i,o)

if __name__ == "__main__":
    main()
