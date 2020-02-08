# -*- coding: utf-8 -*-
"""
Formatierung von Zahlen
"""

artikel = {'Brot': 1.23, 'Mais': 2.20, 'Wurst': 10.78, 'Katzenfutter': 123.99}

print('{1:<13s} | {0:>10s}'.format('Preis', 'Artikel'))
print('-'*26)
for k, v in artikel.items():
    print('{a:<12s}  | {p:>10.2f} '.format(a=k, p = v)) 
    
 