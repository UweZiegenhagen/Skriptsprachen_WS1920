# -*- coding: utf-8 -*-
# einfache Verschlüsselung, nicht für den Einsatz empfohlen
lipsum = """
Hallo. Ich bin ein kleiner Blindtext. Und zwar schon so lange ich denken kann. 
Es war nicht leicht zu verstehen, was es bedeutet, ein blinder Text zu sein: 
Man ergibt keinen Sinn. Wirklich keinen Sinn. Man wird zusammenhangslos 
eingeschoben und rumgedreht – und oftmals gar nicht erst gelesen. Aber bin ich 
allein deshalb ein schlechterer Text als andere? Na gut, ich werde nie in den 
Bestsellerlisten stehen. Aber andere Texte schaffen das auch nicht. Und darum 
stört es mich nicht besonders blind zu sein. Und sollten Sie diese Zeilen noch 
immer lesen, so habe ich als kleiner Blindtext etwas geschafft, wovon all die 
richtigen und wichtigen Texte meist nur träumen.
"""

def encrypt(text, key):
    kodierter_text = ''
    for zeichen in text:
        temp = ord(zeichen)
        temp = temp << key
        temp = chr(temp)
        kodierter_text += temp
    return kodierter_text

geheimtext = encrypt(lipsum,5)
print(geheimtext)


def decrypt(codedtext, key):
    ergebnis = ''
    for geheimzeichen in codedtext:
        temp = ord(geheimzeichen)
        temp = chr(temp >> key)
        ergebnis += temp
    return ergebnis
    
print(decrypt(geheimtext,5))    