# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 20:04:24 2019

@author: Uwe
"""


p = 3.1415927

print('%4.2f %5.4f' % (p, p))
print('%10.2f %5.4f' % (p, p))
print('%10.4f %5.4f' % (p, p))


print('\nArtikel{p:>6d}Euro'.format(p=123))
# Artikel 123 Euro
print('Artikel{p:<6d}Euro'.format(p=123))
# Artikel 123 Euro
print('Artikel{p:^6d}Euro'.format(p=123))
# Artikel 123 Euro
print('Artikel{p:0=6d}Euro'.format(p=123))
# Artikel 000123 Euro
print('Artikel{p:#=6d}Euro'.format(p=123))
# Artikel ###123 Euro
    
print('\nArtikel{p:=+6d}Euro'.format(p=123))
print('Artikel{p:=-6d}Euro'.format(p=-123))
print('Artikel{p:=-6d}Euro'.format(p=123))
print('Artikel{p:= d}Euro'.format(p=-123))
print('Artikel{p:= d}Euro'.format(p=123))

hoehe = 35
breite = 25
print(f'{hoehe} * {breite} = ', hoehe * breite)

