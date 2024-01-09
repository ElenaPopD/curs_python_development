# print("unu")
# print("unu", "doi")
# print("unu", "doi", "trei")

def inmultire(a, b):
    return a * b

inmultire(5, 3)
#inmultire(5, 3, 10)

def inmultire(*args):
    print(args)
    print(type(args))
    produs = 1
    for element in args:
        produs *= element
    return produs


rezultat = inmultire(5, 3, 10)
rezultat = inmultire(5, 3, 10, 20, 100, 30)
print(rezultat)
