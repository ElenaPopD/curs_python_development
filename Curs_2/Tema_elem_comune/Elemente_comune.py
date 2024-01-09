# Avand doua liste, afisati o lista a elementelor comune ambelor liste

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

elemente_comune = [element for element in a if element in b]
print(elemente_comune)

# elemente comune fara duplicate:
elemente_comune_fara_dupl = list(set(a) & set(b))
print(elemente_comune_fara_dupl)   