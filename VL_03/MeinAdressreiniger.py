# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 11:11:55 2019

@author: Uwe
"""

# Lade die Datei schreibgeschützt als Textdatei
with open('Datensatz.txt', 'rt', encoding='utf-8') as eingabedatei:
    for zeile in eingabedatei:
        
        print(zeile, end='') # Gib die Zeile ohne extra Zeilenumbruch aus
        
        if zeile[:-1] == '\n':
            zeile = zeile[:-1] # Entferne Zeilenumbruch, falls vorhanden
        gesplittet = zeile.split(' ') # Splitte anhand des Leerzeichens
        print(gesplittet) # gibt die Liste aus
        
        if gesplittet[-1].isdigit():
            print("Zahl hinten")