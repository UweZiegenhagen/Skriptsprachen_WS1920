# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 15:18:07 2019

@author: Uwe
"""

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

def monate2(zahl):
    if zahl in [1,3,5,7,8,10,12]:
        print(31)
    elif zahl == 2:
        print(28)
    else: 
        print(30)
        
monate2(12)    

def monate3(wert):
    if isinstance(wert,int):
        if wert in [1,3,5,7,8,10,12]:
            print(31)
        elif wert == 2:
            print(28)
        else: 
            print(30)
    else:
        if wert in ['Januar', 'Dezember']:
            print(31)
monate3(12)
monate3('Dezember')

    