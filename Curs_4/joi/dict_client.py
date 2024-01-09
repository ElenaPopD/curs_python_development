from curs4.joi.forme import Cerc

cerc1 = Cerc(raza=5)
print(cerc1.__dict__)
# Antipattern
cerc1.__dict__.pop("raza")
print(cerc1.__dict__)
print(cerc1.raza)