# -*- coding: utf-8 -*-
"""
Rechnet für einen Bruttozinsbetrag KESt, Soli und den Netto-Betrag aus
"""

def berechne_steuern(bruttozinsertrag):
    kapitalertragssteuer = 0.25 * bruttozinsertrag
    solibeitrag = 0.055 * kapitalertragssteuer
    nettozinsertrag = bruttozinsertrag - kapitalertragssteuer - solibeitrag
    return kapitalertragssteuer, solibeitrag, nettozinsertrag


brutto = 100
k, s, n = berechne_steuern(brutto)

print('Für einen Bruttozinsertrag von ', brutto)
print('bezahlt man ', k, 'Euro KESt')
print('bezahlt man ', s, 'Euro Soli')
print('und hat am Ende', n)

    

