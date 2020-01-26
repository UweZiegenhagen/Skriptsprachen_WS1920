"""

print(pd.pivot_table(ordersdetails, index='OrderID',values='Value',
columns='Discount',aggfunc=np.sum, margins=True))

"""


import pandas as pd
import numpy as np

df = pd.read_excel('Verkaufszahlen.xlsx')
print(df)

pt = pd.pivot_table(df, values='Umsatz', index='Jahr', aggfunc=np.sum)
print(pt)

pt = pd.pivot_table(df, values='Umsatz', index='Bereichsleiter', aggfunc=np.sum)
print(pt)