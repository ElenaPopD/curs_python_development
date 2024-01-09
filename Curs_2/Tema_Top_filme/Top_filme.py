 #Lista cu utilizatori si filmele vizionate
utilizatori = [
    {'nume': 'George', 'filme': ['Shrek', 'Bond', 'Fight Club']},
    {'nume': 'Cristian', 'filme': ['Fight Club', 'The Nun', 'Dracula', 'Bond']},
    {'nume': 'Stefan', 'filme': ['Fight Club', 'Slumdog Milionare']}
]

# Dictionare pentru a stoca nr de filme vizionate de fiecare utilizator si nr de viz ale fiecarui film
top_friends = {}
top_movies = {}


for utilizator in utilizatori:
    # Numaram filmele pentru fiecare utilizator
    nume = utilizator['nume']
    numar_filme = len(utilizator['filme'])
    top_friends[nume] = numar_filme

    # Numaram vizionările pentru fiecare film
    for film in utilizator['filme']:
        if film not in top_movies:
            top_movies[film] = 0
        top_movies[film] += 1

#  filmul cel mai vizionat
max_vizionari = -1
cel_mai_vizionat_film = ''
for film, vizionari in top_movies.items():
    if vizionari > max_vizionari:
        max_vizionari = vizionari
        cel_mai_vizionat_film = film

#  utilizatorul cu cele mai multe filme vizionate
max_filme_vizionate = -1
utilizator_max_filme = ''
for nume, numar_filme in top_friends.items():
    if numar_filme > max_filme_vizionate:
        max_filme_vizionate = numar_filme
        utilizator_max_filme = nume

print('Cel mai vizionat film:', cel_mai_vizionat_film)
print('Utilizatorul cu cele mai multe filme vizionate:', utilizator_max_filme)

# Extra
# Top filme dupa vizionari: Fight Club, Bond, Dracula, Shrek, The nun ...
# Dictionar toate filmele și numărul de vizionări
top_filme = {}
for utilizator in utilizatori:
    for film in utilizator['filme']:
        if film in top_filme:
            top_filme[film] += 1
        else:
            top_filme[film] = 1

# Sortam filmele dupa nr  de vizionari
list_filme = [(nr_vizionari, film) for film, nr_vizionari in top_filme.items()]
list_filme.sort(reverse=True)

# afisam topul filmelor
print("Top filme după vizionari:")
for (nr_vizionari, film) in list_filme:
    print(film)
# Top utilizatori cu cele mai multe filme vizionate - Cristian, George, Stefan
# dict cu utilizatorii si nr  de filme pe care le-au vizionat
top_utilizatori = {utilizator['nume']: len(utilizator['filme']) for utilizator in utilizatori}

# Sortam utilizatorii dupa nr de filme vizionate
list_utilizatori = [(nr_filme, nume) for nume, nr_filme in top_utilizatori.items()]
list_utilizatori.sort(reverse=True)

#  topul utilizatorilor
print("\nTop utilizatori cu cele mai multe filme vizionate:")
for (nr_filme, nume) in list_utilizatori:
    print(nume)