# -*- coding: utf-8 -*-

import re

with open('Regexp_blindtext.txt', encoding='utf8') as eingabe:
    text = eingabe.read()
    
    fundstellen = re.findall(r'[A-ZÄÖÜ]{2}[a-züäö]+', text)
     
    for fundstelle in fundstellen:
        ersatz = fundstelle.capitalize()
        text = text.replace(fundstelle, ersatz)
        
    with open('text_gefixt.txt', 'wt', encoding='utf8') as ausgabe:
        ausgabe.write(text)
    