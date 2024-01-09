from random import randrange


class Jucator():
    
    def __init__(self, nume, sold=1000):
        self.nume  = nume
        self.sold = sold 
        self.pozitie = 0 
        self.proprietati =[]
        
    def da_cu_zarul(self):
        return randrange(2,12)
    
    def __repr__(self):
        return f"<Jucator {self.nume}, sold {self.sold}>"
    
    def iesire_din_joc(self):
        self.sold = 0
        for proprietate in self.proprietati:
            proprietate.proprietar = None

    def are_tot_judetul(self, judet) -> bool:
        cartier = [proprietate for proprietate in self.proprietati if hasattr(proprietate, 'judet') and proprietate.judet == judet]
        if len(cartier) > 0:
            return len(cartier) == cartier[0].terenuri_in_judet
        return False
        
class Casuta:
    
    def visit(self, jucator: Jucator):
        print(f"{jucator} a ajuns pe {self}")


class Start(Casuta):

    def visit(self, jucator: Jucator):
        print(f"{jucator} a ajuns pe {self}")
        jucator.sold += 50

class Proprietate(Casuta):
    
    def __init__(self, nume, pret = 500, chirie = 100):
        self.nume = nume
        self.pret = pret
        self._chirie = chirie
        self.proprietar = None
        
    def __repr__(self):
        return f"< {self.__class__.__name__},  {self.nume}>"
    
    @property
    def chirie(self):
        return self._chirie
    
    def visit(self, jucator: Jucator):
        print(f"{jucator} a ajuns pe {self}")
        if self.proprietar is  None:
            self._cumpara(jucator)
        else:
            self._inchiriaza(jucator)
        
    
    def _cumpara(self, jucator: Jucator):
        if jucator.sold < self.pret:
            print(f"Jucatorul { jucator.nume } nu are bani sa cumpere {self}")
            return
        self.proprietar = jucator
        jucator.sold = jucator.sold - self.pret
        jucator.proprietati.append(self)
        print(f"Jucatorul { jucator.nume } a cumparat proprietatea {self.nume}")
    
    def _inchiriaza(self, jucator: Jucator):
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

    PRET_CASUTA = 50
    PRET_HOTEL = 100
    
    def __init__(self, nume, judet, pret=500, chirie=100, terenuri_in_judet=3):
        super().__init__(nume, pret, chirie)
        self.judet = judet
        self.terenuri_in_judet = terenuri_in_judet
        self.casute = 0
        self.hotel = 0

    def _construieste(self):
        if self.casute < 4:
            if self.proprietar.sold > self.PRET_CASUTA:
                self.casute +=1
                self.proprietar.sold -= self.PRET_CASUTA
                print(f"{self.proprietar} a facut o casuta pe {self}")
            else:
                print(f"{self.proprietar} nu are bani sa faca o casuta pe {self}")

    def visit(self, jucator:Jucator):
        if self.proprietar == jucator and jucator.are_tot_judetul(self.judet):
            self._construieste()
        super().visit(jucator)

    @property
    def chirie(self):
        if self.casute > 1:
            return self._chirie * self.casute
        elif self.casute == 1:
            return self._chirie + 5
        return self._chirie

class Gara(Proprietate):
    pass

class Utilitati(Proprietate):
    pass

class Inchisoare(Casuta):
    pass



