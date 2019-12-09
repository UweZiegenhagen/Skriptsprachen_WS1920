# -*- coding: utf-8 -*-

"""
Schreibe eine einfache Telefonbucherfassung, die vom Nutzer Name und
Telefonnummer einliest und diese Informationen in 'Telefonbuch.txt'
abspeichert (anhängt).

"""

name = input('Geben Sie den Namen ein: ')
telefon = input('Geben Sie die Telefonnummer ein: ')

with open('Telefonbuch.txt','a') as tb:
    tb.write(name + ':' + telefon + '\n')