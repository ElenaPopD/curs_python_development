from curs4.joi.forme import Cerc, Dreptunghi

cerc1 = Cerc(raza=3)
dreptunghi1 = Dreptunghi(3,4)

cerc2 = Cerc(raza=5)
dreptunghi2 = Dreptunghi(10, 10)

cerc3 = Cerc(raza=1)

lista_forme = [cerc1, cerc2, cerc3, dreptunghi1, dreptunghi2]

# cerc1 < cerc2  -> cerc1.__lt__(cerc2)
print(cerc2 < cerc3)
print(cerc2 > cerc3)
print(cerc2 == cerc3)
dreptunghi2.deseneaza()
cerc1.deseneaza()

print(sorted(lista_forme))
