# -*- coding: utf-8 -*-
"""
Bestimmt die Anzahl der Tage ausgehend vom Monat
"""

# Einfacher Ansatz
def monate1(zahl):
    if zahl == 1:
        return 31
    if zahl == 2:
        return 28
    if zahl == 3:
        return 31
    if zahl == 4:
        return 30
    if zahl == 5:
        return 31
    if zahl == 6:
        return 30
    if zahl == 7:
        return 31
    if zahl == 8:
        return 31
    if zahl == 9:
        return 30
    if zahl == 10:
        return 31
    if zahl == 11:
        return 3
    if zahl == 12:
        return 31    

print(monate1(12))

#besser!
def monate2(zahl, jahr=2019):
    if zahl in [1,3,5,7,8,10,12]:
        print(31)
    elif zahl == 2:
         # https://trainyourprogrammer.de/python-31-schaltjahresberechnung.html
         if jahr % 4 == 0: # vielleicht ein Schaltjahr
             if jahr % 100 == 0: # vermutlich kein Schaltjahr
                 if jahr % 400 == 0: # doch ein Schaltjahr
                     print(29)
                 else:
                     print(28)
             else:
                 print(29)
         else:
             print(28)
    else: 
        print(30)
        
# Schaltjahre
monate2(2, 1664)
monate2(2, 1600)
monate2(2, 2000)
monate2(2, 2004)
# keine Schaltjahre
monate2(2, 1003)
monate2(2, 2006)
monate2(2, 1700)
monate2(2) # 2019

# für Zahlen und Namen
def monate3(wert):
    if isinstance(wert,int):
        if wert in [1,3,5,7,8,10,12]:
            print(31)
        elif wert == 2:
            print(28)
        else: 
            print(30)
    elif isinstance(wert,str):
        if wert in ['Januar', 'März', 'Mai', 'Juli', 
                    'August', 'Oktober', 'Dezember']:
            print(31)
        elif wert in ['Februar']:
            print(28)
        else:
            print(30)
    else:
        print('String oder integer übergeben!')

for i in range(13):
    monate3(i)

for i in ('Mai', 'Juni'):
    monate3(i)

monate3(3.1245345) # Fehler, da kein String oder int