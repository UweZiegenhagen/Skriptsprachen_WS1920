# -*- coding: utf-8 -*-

import pprint #1
import pprint as p #2

text = 'Hallo FOM\n\r\f, ich bin ein etwas längerer Satz, der als Beispiel für einen Counter dient'

d = {}

for i in text:
    print(d.keys())
    if i in d.keys():
        d[i] = d[i] + 1 
    else:
        d[i] = 1

pprint.pprint(d) #1
