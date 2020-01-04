# -*- coding: utf-8 -*-

import re

with open('Regexp_blindtext.txt', encoding='utf8') as eingabe:
    text = eingabe.read()
    
    text_neu = re.sub(r'\s+\d+', '', text)
    
    with open('text_neu.txt', 'wt', encoding='utf8') as ausgabe:
        ausgabe.write(text_neu)