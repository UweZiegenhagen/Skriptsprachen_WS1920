# -*- coding: utf-8 -*-
"""
Rekursive Ermittlung von Endkapital
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
