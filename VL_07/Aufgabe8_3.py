# -*- coding: utf-8 -*-


with open('BeliebigeTextdatei.txt', 'r') as lese:
    with open('Ziel.txt', 'w') as schreibe:
        for line in lese:
            schreibe.write(line)