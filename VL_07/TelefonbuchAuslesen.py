# -*- coding: utf-8 -*-


with open('Telefonbuch.txt','rt') as tb:
    for eintrag in tb:
        name, nummer = eintrag.split(':')
        print(name, 'hat die Nummer', nummer[:-1])