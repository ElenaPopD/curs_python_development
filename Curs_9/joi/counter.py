from collections import Counter

a = Counter("ana are mere")
print(a)
print(a.most_common(3))


prieteni = [
    {'nume': 'George', 'filme': ["Top Gun", "Wonka"]},
    {'nume': 'Ionel', 'filme': ["Top Gun", "Wonka",3,4]},
    {'nume': 'Gica', 'filme': [2,3,4,5,6]}
]

# Varianta 1
top_filme = Counter() #empty counter
for prieten in prieteni:
    top_filme.update(prieten["filme"]) # update cu filmele unui prieten


# Varianta 2 
toate_filmele = [film for prieten in prieteni for film in prieten["filme"]]

toate_filmele = []
for prieten in prieteni:
    for film in prieten["filme"]:
        toate_filmele.append(film)

print("Toate filmele", toate_filmele)
top_filme = Counter(toate_filmele)

print(top_filme)
print(top_filme.most_common(3))