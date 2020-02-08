# -*- coding: utf-8 -*-
"""
Variable Zahl an Parametern

"""

def multipliziere(*args):
    ergebnis = 1
    for number in args:
        ergebnis *= number
    return ergebnis
    
def potenziere(*args):
    ergebnis = args[0]
    for number in args:
        ergebnis = ergebnis ** number
    return ergebnis    
  
print(multipliziere(1, 2, 3, 4, 5))
print(potenziere(2, 3, 4, 5))