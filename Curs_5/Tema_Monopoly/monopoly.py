from random import randrange
class Casuta:
    
    def visit(self, jucator):
        print(f"{jucator} a ajuns pe {self}")

class Jucator():
    
    def __init__(self, nume, sold=1000):
        self.nume  = nume
        self.sold = sold 
        self.pozitie = 0 
        self.proprietati =[]
        self.runde_in_inchisoare = 0
        
    def da_cu_zarul(self):
        return randrange(2,12)
    
    def __repr__(self):
        return f"<Jucator {self.nume}, sold {self.sold}>"
    
    def iesire_din_joc(self):
        self.sold = 0
        for proprietate in self.proprietati:
            proprietate.proprietar = None
    
        
    

class Start(Casuta):
    def visit(self, jucator):
        print(f"{jucator} a ajuns pe {self}")
        jucator.sold += 50

class Proprietate(Casuta):
    
    def __init__(self, nume, pret = 500, chirie = 100):
        self.nume = nume
        self.pret = pret
        self.chirie = chirie
        self.proprietar = None
        
    def __repr__(self):
        return f"< {self.__class__.__name__},  {self.nume}>"
        
        
    def visit(self, jucator):
        print(f"{jucator} a ajuns pe {self}")
        if self.proprietar is  None:
            self._cumpara(jucator)
        else:
            self._inchiriaza(jucator)
        
    
    def _cumpara(self, jucator):
        self.proprietar = jucator
        jucator.sold = jucator.sold - self.pret
        jucator.proprietati.append(self)
        print(f"Jucatorul { jucator.nume } a cumparat proprietatea {self.nume}")
    
    def _inchiriaza(self, jucator):
        if self.proprietar == jucator:
            return
        if jucator.sold - self.chirie > 0:
            self.proprietar.sold += self.chirie    
            jucator.sold = jucator.sold - self.chirie
            print(f"Jucatorul { jucator.nume } plateste chirie lui{self.proprietar}")
        else:
            self.proprietar.sold += jucator.sold   
            jucator.iesire_din_joc()
            print(f"Jucatorul { jucator.nume } iese din joc")

    
class Teren(Proprietate):
    def _inchiriaza(self, jucator):
        # Verifică dacă proprietarul deține toate cele 4 proprietăți Teren
        if len([p for p in self.proprietar.proprietati if isinstance(p, Teren)]) == 4:
            chiria = self.chirie * 2
        else:
            chiria = self.chirie

class Gara(Proprietate):
    def _inchiriaza(self, jucator):
        # Verifică dacă proprietarul deține ambele Gări
        if len([p for p in self.proprietar.proprietati if isinstance(p, Gara)]) == 2:
            chiria = self.chirie * 2
        else:
            chiria = self.chirie

class Utilitati(Proprietate):
    def _inchiriaza(self, jucator):
        # Verifică dacă proprietarul deține toate cele 3 Utilități
        if len([p for p in self.proprietar.proprietati if isinstance(p, Utilitati)]) == 3:
            chiria = self.chirie * 3
        else:
            chiria = self.chirie

class Inchisoare(Casuta):
    def visit(self, jucator):
        print(f"{jucator} este în închisoare.")
        jucator.runde_in_inchisoare = 3  # De exemplu, jucătorul stă 3 runde în închisoare



