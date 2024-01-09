import random
class Teren:
    def __init__(self, nume):
        self.nume = nume
        self.numar_casute = 0

    def construieste_casuta(self):
        if self.numar_casute < 4 and random.randint(2, 12) > 8:
            self.numar_casute +=1
            return True
        return False
    
    def __repr__(self):
        return f"Teren {self.nume} <{self.numar_casute}>"

proprietati = [Teren(1), Teren(2), Teren(3)]

def construieste(teren: Teren) -> bool:
    return teren.construieste_casuta()

for reusit in map(construieste, proprietati):
    if reusit:
        print("Am construit")
    else:
        print("Nu s-a construit")

print(proprietati)