# -*- coding: utf-8 -*-
"""

Wenn man die Aufgabe 1 so interpretiert, dass die Frage lautet

"Wie oft ist der Buchstabe 'z' in einem String s enthalten?"

da könnte die Lösung so aussehen:

"""

def anzahl_der_zs(s):
    return len(s) - len(s.replace('z',''))

print(anzahl_der_zs('Szdf zegfzdf'))