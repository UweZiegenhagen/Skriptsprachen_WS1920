# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 14:42:18 2019

@author: Uwe
"""

def endkapital(startkapital, zins, jahre):
    return startkapital * (1+zins)**jahre

def vergleiche(startkapital, zins1, zins2, jahre):
    k1 = endkapital(startkapital,zins1, jahre)
    k2 = endkapital(startkapital,zins2, jahre)
    return k2 - k1    


print(endkapital(100, 0.1, 100))
print(endkapital(100, 0.11, 100))
print(vergleiche(100, 0.1, 0.11, 100))
    