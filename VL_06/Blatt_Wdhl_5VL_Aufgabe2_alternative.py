# -*- coding: utf-8 -*-
""" 

Eine alternative Lösung der Frage,
welche Zeichen sind in String 1 und in 
String 2 enthalten.

"""

st1 = 'Hallo FOM, viele Grüße aus Köln'
st2 = 'Nett hier. Aber waren Sie schon mal in Baden-Würtemberg?'

d = {}
e = {}

for i in st1:
    if i in d.keys():
        d[i] = d[i] + 1 
    else:
        d[i] = 1

for i in st2:
    if i in e.keys():
        e[i] = e[i] + 1 
    else:
        e[i] = 1

k1 = list(d.keys())
k2 = list(e.keys())

result = []

for c in k1:
    if c in k2:
        result.append(c)
        
for c in k2:
    if c in k1 and c not in result:
        result.append(c)
        
print(result)