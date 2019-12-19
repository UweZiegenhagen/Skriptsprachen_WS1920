class Point():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance_euc(self, p):
        return ((p.y - self.y)**2 + (p.x - self.x)**2)**0.5
    
    def distance_city(self, p):
        return abs(p.y - self.y) +  abs(p.x - self.x)

  
p = Point(2, 2)
x = Point(1, 1)

print(x.distance_euc(p))
print(x.distance_city(p))