a = [1, 2, 3]
#    0  1  2
b = a[:] # a.copy()
print(a, b)
print(a is b)
# lista[start:end:step]
print(a[1:2])
b = list(range(10, 20))
print(b)
print(b[1:3])
c = list(range(10))
print(c)
print(c[::3])

# De la pozitia 1 pana la sfarsit
print(c[1:])

# Pana la o anume pozitie
print(c[:3])

print(c[2:])
print(c[2::3])
