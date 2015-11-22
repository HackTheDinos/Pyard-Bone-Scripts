#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Give a root directory (ideally some type of animal).
If the animal has more than 1 *.doc file it joins them together
"""

import subprocess
import os
import argparse

ALL_DATA = []

def parse():
    p = argparse.ArgumentParser()
    p.add_argument('dir', help = 'root directory')
    d = p.parse_args()
    return d.dir


def walk(d = '.'):
    for root, dirs, files in os.walk(d):
        for i in files:
            if '.doc' in i:
                o = os.path.join(root, i)
                print(o)
                try:
                    s = subprocess.check_output(['catdoc', o])
                    s = s.decode('UTF-8')
                    global ALL_DATA
                    ALL_DATA.append(s)
                except Exception as e:
                    print("Doesn't Work")
                    print(e)

    notes_string = "\n NewFile \n".join(ALL_DATA) 
    return {'notes' : notes_string}

if __name__ == '__main__':
    walk(parse())



