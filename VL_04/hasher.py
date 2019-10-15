# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 18:46:21 2019

@author: Uwe
"""

import hashlib

geheimer_text = hashlib.md5('9876543'.encode()).hexdigest()

for i in range(100000000):
    m = hashlib.md5(str(i).encode())
    if m.hexdigest() == geheimer_text:
        print(i , 'ist das Passwort')
        break
