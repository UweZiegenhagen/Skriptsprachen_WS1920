# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 09:24:21 2019

@author: Uwe
"""

def gib_die_zahl_aus(text):
    for i in text:
        print(i,':',ord(i))

gib_die_zahl_aus('Hallo FOM')

def gib_das_zeichen_aus():
    for i in (range(1,200)):
        print(i,':',chr(i))

gib_die_zahl_aus('Hallo FOM')

gib_das_zeichen_aus()