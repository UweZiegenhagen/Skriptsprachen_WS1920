# einfache Funktionen zum Zentrieren eines Strings

def zentriere_string(text):
    print(text.center(60, '.'))
    

zentriere_string('Uwe')
zentriere_string('UweUwe')
zentriere_string('Katze')

def zentriere_string2(text):
    text = text.strip()
    laenge = 60 - len(text)
    laenge= int(laenge / 2)
    print('.' * laenge + text + '.'* laenge)
    
    
zentriere_string2('Uwe')
zentriere_string2('UweUwe')
zentriere_string2('Katze')
    