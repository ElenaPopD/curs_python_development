top_filme = {
    'Bond': 2,
    'Dracula': 1,
    'Fight Club': 3,
    'Shrek': 1,
    'Slumdog Milionare': 1,
    'The Nun': 1
}
sortat = [
    ('Fight Club', 3),
    ('Bond', 2),
    ('Shrek', 1)
]
list_filme = []
for (film, nr_vizionari) in top_filme.items():
    list_filme.append((nr_vizionari, film))
print(list_filme)

list_filme.sort(reverse=True)
print(list_filme)
for (nr_vizionari, film) in list_filme:
    print(film)




