# Nutzen von inneren Funktionen, um beliebige Filter zu erstellen
# nicht klausurrelevant, aber interessant anzuschauen
# https://www.linux-magazin.de/ausgaben/2009/10/funktionale-programmierung-2-python-funktional/

zahlenliste = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def filtereZahl(nachZahl):
    def filtere(liste):
        ergebnis = []
        for number in liste:
            if number % nachZahl == 0:
                pass
            else:
                ergebnis.append(number)
        return ergebnis
    return filtere

f3 = filtereZahl(3)

print(f3(zahlenliste))