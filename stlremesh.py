#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import subprocess
import os.path


"""
Script to use the mxl scripts from meshlabserver
to apply filters to the meshes, to compress file
size.

Usage:
    python3 stlremesh.py <input filename> <output filename>
"""

def remesh(i, o):
    script_location = os.path.realpath(__file__)
    script_location = os.path.split(script_location)[0]
    mlx_script = os.path.join(script_location, 'quad.mlx')
    #Quad.mlx uses quad Edge Collapse Decimation
    s = subprocess.call(['meshlabserver', '-i', i, '-o', o, '-s',
                        mlx_script,], stdout = subprocess.DEVNULL,
                        stderr = subprocess.DEVNULL)
    print("Completed file {}".format(o))


def parser_cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Input File')
    parser.add_argument('output', help='Output File')
    p = parser.parse_args()
    return p.input, p.output

def main():
    i, o = parser_cli()
    print("Applying remesh to {}".format(i))
    remesh(i,o)

if __name__ == "__main__":
    main()
