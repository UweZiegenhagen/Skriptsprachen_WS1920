# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 19:39:30 2020

@author: Uwe
"""

import pandas as pd

df = pd.read_excel('Northwind.xlsx', sheet_name  = 'Orders Details')

df = df[['UnitPrice', 'Quantity']]


df['Gesamtpreis'] = df['UnitPrice'] * df['Quantity']  

df = df[df['Gesamtpreis'] < 50]


print(df)