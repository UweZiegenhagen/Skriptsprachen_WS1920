# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 11:11:55 2019

@author: Uwe
"""


with open('Datensatz.txt', 'rt', encoding='utf-8') as eingabedatei:
    for zeile in eingabedatei:
        print(zeile, end='')
        gesplittet = zeile[:-1].split(' ')
        print(gesplittet)
        
        if gesplittet[-1].isdigit():
            print("Zahl hinten")