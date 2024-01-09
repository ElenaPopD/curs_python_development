from collections import ChainMap
from itertools import chain

a = [1,2,3]
b = {4,5,6}
c = {"cheie": "valoare", "cheie2": "valoare2"}

for item in chain(a,b,c):
    print(item)


print("Chain map:")
a = {1:"unu"}
b = {2: "doi"}
c = {3: "trei", 2:"doi din c"}

for key, value in ChainMap(a,b,c).items():
    print(key, value)

