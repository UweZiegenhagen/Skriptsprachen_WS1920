# -*- coding: utf-8 -*-

import pprint

text = 'Hallo FOM, ich bin ein etwas längerer Satz, der als Beispiel für einen Counter dient'

d = {}

for i in text:
    if i in d.keys():
        d[i] = d[i] + 1 
    else:
        d[i] = 1

pprint.pprint(d)