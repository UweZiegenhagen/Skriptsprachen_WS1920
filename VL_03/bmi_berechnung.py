# -*- coding: utf-8 -*-
"""
BMI = Gewicht in Kg / (Größe in m)^2
"""

def berechne_bmi(name, gewicht, groesse):
    return name, gewicht/groesse**2

name, bmi = berechne_bmi('Donald', 80, 2)

print(name, 'hat einen BMI von', bmi)

def berechne_bmi_interaktiv():
    groesse = input('Geben Sie die Größe in m an: ')
    gewicht = input('Geben Sie das Gewicht in Kg an: ')
    name = input('Name: ')
    groesse = float(groesse)
    gewicht = float(gewicht)
    print('Hallo', name)
    print('Dein BMI beträgt:', gewicht/groesse**2)
    
#berechne_bmi()

