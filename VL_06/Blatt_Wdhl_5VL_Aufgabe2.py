# -*- coding: utf-8 -*-
"""
set() erstellt pro String die Menge der unique Zeichen.

Mit der intersection() Funktion bzw. dem intersection & Operator
erhält man die Schnittmenge der Zeichen, die sowohl in set 1 als
auch in set 2 enthalten sind. 

"""

st1 = 'Hallo FOM, viele Grüße aus Köln'
st2 = 'Nett hier. Aber waren Sie schon mal in Baden-Würtemberg?'

s1 = set(st1)
s2 = set(st2)

print(s1.intersection(s2))

print(s1 & s2)