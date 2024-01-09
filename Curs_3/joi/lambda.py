sortat = [
    ('Bond', 2),
    ('Fight Club', 3),
    ('Shrek', 1)
]
def sort_criteria(element):
    film, vizionari = element
    return vizionari

print(sorted(sortat, key=sort_criteria, reverse=True))

print(sorted(sortat, key=lambda x: x[1], reverse=True))
