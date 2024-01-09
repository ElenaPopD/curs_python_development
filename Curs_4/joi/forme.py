class Forma(object):

    def __lt__(self, other):
        if self.aria() < other.aria():
            return True
        else:
            return False
        
    def __repr__(self):
        return f"<{self.__class__.__name__} {self.aria()}>"
    
    def deseneaza(self):
        print("Desenez")

    def __eq__(self, other):
        return self.aria() == other.aria()

    def __hash__(self):
        # return id(self)
        return int(self.aria())

class Cerc(Forma):
    PI = 3.14

    def __init__(self, raza):
        self.raza = raza

    def aria(self):
        return self.PI * (self.raza ** 2)
    
    def deseneaza(self):
        
        print("Deseneaza cerc")

class Dreptunghi(Forma):
    
    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2

    def aria(self):
        return self.l1 * self.l2
    
    @classmethod
    def patrat(cls, l):
        return cls(l1=l, l2=l)
    
    @staticmethod
    def e_patrat(l1, l2):
        print(l1, l2)
        return l1 == l2

    