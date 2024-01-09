from functools import partial

def sum(a, b, putere):
    return (a+b) ** putere

la_patrat = partial(sum, putere=2)

#print(type(la_patrat))
print(la_patrat(2,3))

cub = partial(sum, putere=3)


print(cub(2,3))

def la_a_treia(a,b):
    return sum(a,b, 3)

print(la_a_treia(2,3))

