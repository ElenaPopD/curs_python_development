from random import randrange
class Casuta:
    
    def visit(self, jucator):
        print(f"{jucator} a ajuns pe {self}")

class Jucator():
    
    def __init__(self, nume, sold=1000):
        self.nume  = nume
        self.sold = sold 
        self.pozitie = 0 
        
    def da_cu_zarul(self):
        return randrange(2,12)
    
    def __repr__(self):
        return f"<Jucator {self.nume}>"
    
        
    

class Start(Casuta):
    pass

class Proprietate(Casuta):
    
    def __init__(self, nume):
        self.nume = nume
    
class Teren(Proprietate):
    pass

class Gara(Proprietate):
    pass

class Utilitati(Proprietate):
    pass

class Inchisoare(Casuta):
    pass



