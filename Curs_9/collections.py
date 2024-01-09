prieteni = [
    {'nume': 'George', 'filme': ["Top Gun", "Wonka"]},
    {'nume': 'Ionel', 'filme': ["Top Gun", "Wonka",3,4]},
    {'nume': 'Gica', 'filme': [2,3,4,5,6]}
]

# cele mai multe filme
{
    "George":3,
    "Ionel": 4,
    "Gica": 5
}

for i in prieteni:
    print(i["nume"], len(i["filme"]))

cinefili = { prieten["nume"]: len(prieten["filme"]) for prieten in prieteni }

print(cinefili)

# top filme vizionate
{
    1: 2,
    2: 3,
    3: 3,
    4: 2,
    5: 1,
    6: 1
}

lista_mare = []
for prieten in prieteni:
    lista_mare.extend(prieten["filme"])
print(lista_mare)

top_filme = {film: lista_mare.count(film) for film in lista_mare}
print("top_filme dict_comprehension")
print(top_filme)


top_filme = {}
for prieten in prieteni:
    for film in prieten["filme"]:
        if film in top_filme:
            top_filme[film] += 1
        else:
            top_filme[film] = 1
print("top_filme building dict")
print(top_filme)

from collections import defaultdict

top_filme = defaultdict(lambda: 0)

for prieten in prieteni:
    for film in prieten["filme"]:
        top_filme[film] += 1
print("top_filme building dict")
print(top_filme[1]) # top_filme[1] = 0 
print(top_filme)