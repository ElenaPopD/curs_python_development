class Masina:
    NUMAR_USI = 5

    def __init__(self, nume, an=2000):
        self.nume = nume
        self.an = an

    def claxon(self):
        print(f"{self.nume} Tit tit")

dacia = Masina("Dacia", 1997)
renault = Masina("Renault", 2010)


print(dacia.nume)
print(renault.nume)
dacia.claxon()
renault.claxon()#renault)


dacia.motor = 1310
print(dacia.motor)
#print(renault.motor)
import pdb; pdb.set_trace()


# print(dacia, type(dacia), id(dacia))
# print(renault, type(renault), id(renault))