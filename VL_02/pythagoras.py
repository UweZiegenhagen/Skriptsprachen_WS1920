# -*- coding: utf-8 -*-
"""
Ermittlung der Hypothenuse eines rechtwinkligen Dreiecks
"""

def pythagoras(kathete1, kathete2):
    return (kathete1**2 + kathete2**2)**0.5
    
print(pythagoras(3, 4))