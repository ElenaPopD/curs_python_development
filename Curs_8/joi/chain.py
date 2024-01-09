from itertools import chain
a = [1,2,3]
b = {4,5,6}
c = (7,8,9)

for val in chain(a,b,c):
    print(val)

# print(len(chain(a,b,c)))
any((
    2 in a,
    2 in b,
    2 in c
))

2 in chain(a,b,c)

lista_element = []
lista_element.extend(a)
lista_element.extend(b)
lista_element.extend(c)

print(2 in lista_element)