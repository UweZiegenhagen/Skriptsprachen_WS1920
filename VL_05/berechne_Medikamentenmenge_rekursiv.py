# -*- coding: utf-8 -*-

def berechne_medikamentenmenge(n):
    menge = 0
    if n == 0:
        menge = 5
    else:
        menge = 5 + berechne_medikamentenmenge(n-1) * 0.6
    
    return menge

print(berechne_medikamentenmenge(0))
print(berechne_medikamentenmenge(1))
print(berechne_medikamentenmenge(2))
print(berechne_medikamentenmenge(10))
print(berechne_medikamentenmenge(100))
print(berechne_medikamentenmenge(1000))
print(berechne_medikamentenmenge(2000))
