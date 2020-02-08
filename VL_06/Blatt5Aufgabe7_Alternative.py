# -*- coding: utf-8 -*-
# Alternative über "collection" aus dem collections Modul

import collections
import pprint

text = 'Hallo FOM, ich bin ein etwas längerer Satz, der als Beispiel für einen Counter dient'

c = collections.Counter(text)

pprint.pprint(c)