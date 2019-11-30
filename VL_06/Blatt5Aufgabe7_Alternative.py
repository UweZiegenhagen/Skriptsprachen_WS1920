# -*- coding: utf-8 -*-

import collections
import pprint

text = 'Hallo FOM, ich bin ein etwas längerer Satz, der als Beispiel für einen Counter dient'

c = collections.Counter(text)

pprint.pprint(c)