class Konto:
    
    def __init__(self, iban):
        self.iban = iban
        self.kontostand = 0

    def setze_dispo(self, betrag):
        self.dispo = -1 * betrag
        
    def einzahlen(self, betrag):
        self.kontostand += betrag
    
    def auszahlen(self, betrag):
        self.kontostand -= betrag

    def kontostand(self):
        return self.kontostand
    
    def ueberweisen(self, k, betrag):
        if isinstance(k, Konto):
            self.kontostand -= betrag
            k.kontostand += betrag

if __name__ == '__main__':
    k = Konto(12345678)
    finanzamt = Konto(111111111)
    print(k.kontostand)
    k.einzahlen(100)
    print(k.kontostand)
    k.ueberweisen(finanzamt, 10)
    print(k.kontostand)
