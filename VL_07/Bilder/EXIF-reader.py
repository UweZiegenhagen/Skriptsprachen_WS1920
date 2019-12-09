# -*- coding: utf-8 -*-

import exifread
import os

for file in os.listdir("."):
    if file.lower().endswith("7.jpg"):
        with open("./"+file, 'rb') as f:
            print('Datei', file)
            tags = exifread.process_file(f)
            
            for k, v in tags.items():
                print(k, v)
                #if k.startswith('EXIF'):
                #    print(' ',k,v)