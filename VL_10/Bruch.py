class Bruch():
    
    def __init__(self, zaehler, nenner):
        self.zaehler = zaehler
        self.nenner = nenner
        
    def __str__(self):
        return '{}/{}'.format(self.zaehler, self.nenner)
        
    def erweitern(self, zahl):
        if type(zahl) is int:
            return Bruch(self.zaehler * zahl, self.nenner * zahl)
        
    def kuerzen(self, zahl):
        """
            ganzzahlig teilen
        """
        if isinstance(zahl, int):
            if self.zaehler % zahl == 0 or self.nenner % zahl == 0:
                return Bruch(self.zaehler // zahl, self.nenner // zahl)
            else:
                raise ValueError('Nicht restlos teilbar')
        
    def addieren(self, b):
        if isinstance(b, Bruch):
            if self.nenner == b.nenner:
                return Bruch(self.zaehler + b.zaehler, self.nenner)
        else:
            neu_nenner = self.nenner * b.nenner
            return Bruch(self.zaehler * b.nenner+  b.zaehler * self.nenner, neu_nenner)
        
    def subtrahieren(self, b):
        if isinstance(b, Bruch):
            if self.nenner == b.nenner:
                return Bruch(self.zaehler - b.zaehler, self.nenner)
        else:
            neu_nenner = self.nenner * b.nenner
            return Bruch(self.zaehler * b.nenner -  b.zaehler * self.nenner, neu_nenner)
    
    def multiplizieren(self, b):
        if isinstance(b, Bruch):
            return Bruch(self.zaehler*b.zaehler, self.nenner * b.nenner)
        raise TypeError('Kein Bruch übergeben')
    
    def dividieren(self, b):
        if isinstance(b, Bruch):
            return Bruch(self.zaehler*b.nenner, self.nenner * b.zaehler)
        raise TypeError('Kein Bruch übergeben')
    
if __name__ == '__main__':
    b = Bruch(1, 2)
    print(b)
    c = b.erweitern(2)
    print(c)
    d = c.kuerzen(2)
    print(d)
    