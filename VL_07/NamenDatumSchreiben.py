# -*- coding: utf-8 -*-

# Blatt 8, Aufgabe 1
import time

jetzt = time.strftime("%Y-%m-%d", time.localtime())
print(jetzt)

with open('NameDatum.txt','w') as datei:
    datei.write('Uwe ' + jetzt)
