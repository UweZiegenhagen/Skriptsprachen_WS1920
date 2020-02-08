# wenn die Länge restlos durch 3 teilbar ist, drehe das Wort um

def umkehr_drei(text):
    if len(text) % 3 == 0:
        print(text[::-1])

umkehr_drei('Uwe')
umkehr_drei('UweUwe')
umkehr_drei('Katze')