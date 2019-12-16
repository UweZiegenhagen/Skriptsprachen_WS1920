import pprint
werte = {}
jahre = []
bleiter = []

with open('Verkaufszahlen.tsv') as datei:
    for zeile in datei:
        jahr, bereichsleiter, umsatz = zeile.split('\t')
        # wenn ord() des ersten Zeichens >57 ==> ignoriere
        if ord(jahr[0].lower())>57:
            pass
        else:
            umsatz = umsatz[:-1]
            umsatz = umsatz.replace('.','')
            umsatz = umsatz.replace(',','.')
            umsatz = float(umsatz)

            #print(jahr, bereichsleiter, umsatz)
            
            if jahr in werte.keys():
                bisheriger_betrag = werte[jahr]
                neuer_betrag = bisheriger_betrag + umsatz
                werte[jahr] = neuer_betrag
            else:
                werte[jahr] = umsatz
                jahre.append(jahr)

            if bereichsleiter in werte.keys():
                bisheriger_betrag = werte[bereichsleiter]
                neuer_betrag = bisheriger_betrag + umsatz
                werte[bereichsleiter] = neuer_betrag
            else:
                werte[bereichsleiter] = umsatz                
                bleiter.append(bereichsleiter)
                
    for j in jahre:
        print(j, werte[j])
                

    for b in bleiter:
        print(b, werte[b])                