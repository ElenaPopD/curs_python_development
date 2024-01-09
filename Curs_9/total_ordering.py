from functools import total_ordering

@total_ordering
class Cerc:
    
    def __init__(self, raza):
        self.raza = raza

    def aria(self):
        return 3.14 * (self.raza ** 2)
    
    def __lt__(self, other):
        return self.aria() < other.aria()
    

c1 = Cerc(1)
c2 = Cerc(2)

print(c1 < c2)
print(c1 > c2)
print(c1 <= c2)
print(c1 >= c2)
print(c1 == c2)
print(c1 != c2)
