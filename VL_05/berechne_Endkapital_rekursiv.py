# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 19:44:58 2019

@author: Uwe Ziegenhagen
"""

def berechne_endkapital(s0, i, n):
    e = 0
    if n == 0:
        e = s0
    else:
        e = berechne_endkapital(s0, i, n-1) * (1+i)
    
    return e

print(berechne_endkapital(100, 0.1, 1))
print(berechne_endkapital(100, 0.1, 2))

print(berechne_endkapital(100, 0.1, 50))
