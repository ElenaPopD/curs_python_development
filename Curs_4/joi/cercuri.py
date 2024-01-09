from curs4.joi.forme import Cerc

set_cercuri = set()
a = Cerc(3)
print("a =", id(a), hash(a))
set_cercuri.add(a)
b = Cerc(3)
print("b =", id(b), hash(b))
set_cercuri.add(b)
c = Cerc(3)
print("c =", id(c), hash(c))
set_cercuri.add(c)

print(set_cercuri, len(set_cercuri))

my_dict = {a: 1, b: 3, c: 2}

print(my_dict)