class Quadrat():

    def __init__(self, laenge_der_seite = 1):
        self.seitenlaenge = laenge_der_seite

    
    def berechne_umfang(self):
        return 4 * self.seitenlaenge


    def berechne_flaeche(self):
        return self.seitenlaenge**2


q = Quadrat(25)
print(q.berechne_flaeche())
print(q.berechne_umfang())