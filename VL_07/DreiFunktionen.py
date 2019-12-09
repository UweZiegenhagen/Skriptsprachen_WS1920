# -*- coding: utf-8 -*-

zahlenliste = [1, 2, 3, 4, 5, 6, 7, 8, 9]
wortliste = ['abc', 'def', 'ghi']

def filtere(liste):
    ergebnis = []
    for number in liste:
        if number % 2 == 0:
            pass
        else:
            ergebnis.append(number)
    return ergebnis

print(filtere(zahlenliste))


def kapitalisiere(liste):
    ergebnis = []
    for text in liste:
        ergebnis.append(text.capitalize())
    return ergebnis

print(kapitalisiere(wortliste))


def summiereauf(liste):
    ergebnis = 0
    for number in liste:
        ergebnis += number
    return ergebnis
        
print(summiereauf(zahlenliste))


