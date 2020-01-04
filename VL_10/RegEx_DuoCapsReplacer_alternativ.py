# -*- coding: utf-8 -*-
import re

# https://stackoverflow.com/questions/8934477/making-letters-uppercase-using-re-sub-in-python

with open('Regexp_blindtext.txt',encoding='utf8') as eingabe:
    text = eingabe.read()
    
    fundstellen = re.findall(r'[A-Z]{2}[a-z]{1,}', text)
    for fundstelle in fundstellen:
        print(fundstelle)

    text_neu = re.sub(r'([A-Z]{2,}[a-z]{1,})', lambda match: r'{}'.format(match.group(0).capitalize()), text)
    
    with open('Regexp_blindtext_neu.txt','wt') as ausgabe:
        ausgabe.write(text_neu)
        

