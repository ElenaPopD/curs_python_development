

class Proprietate(object):
    
    def __init__(self, nume, pret = 500, chirie = 100):
        self.nume = nume
        self.pret = pret
        self.chirie = chirie
        self.proprietar = None
        self._nr_case = 0
        self._has_hotel = False

    def adauga_casa(self):
        if self._nr_case < 4:
            self._nr_case +=1
            self.proprietar.sold -= 20
        else:
            self.proprietar.sold -= 100
            self._nr_case = 0
            self.has_hotel = True
        

