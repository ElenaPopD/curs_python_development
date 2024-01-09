a = range(4)
suma = 0
for val in map(lambda x: x ** 2, a):
    print(val)
    suma+= val
print(suma)