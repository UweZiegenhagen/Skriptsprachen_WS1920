# -*- coding: utf-8 -*-

def finde_maximum(eine_liste):
    """
        Die einfache Lösung    
    """
    return max(eine_liste)

print(finde_maximum([3, 7, 15, 42, 2, 1, 4, 6]))

def finde_maximum2(eine_liste):
    maximum = eine_liste[0]
    for zahl in eine_liste[1:]:
        if maximum < zahl:
            maximum = zahl
    return maximum

print(finde_maximum2([3, 7, 15, 42, 2, 1, 4, 6]))