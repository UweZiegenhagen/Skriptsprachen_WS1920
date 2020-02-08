# Zahl zu Buchstabe und umgekehrt


def gib_die_zahl_aus(text):
    for i in text:
        print(i,':',ord(i))

gib_die_zahl_aus('Hallo FOM')

def gib_das_zeichen_aus():
    for i in (range(1,200)):
        print(i,':',chr(i))

gib_die_zahl_aus('Hallo FOM')

gib_das_zeichen_aus()