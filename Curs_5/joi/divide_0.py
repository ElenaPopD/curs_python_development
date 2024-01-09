try:
    val = 1/0
    True
except ZeroDivisionError:
    print("Gaura neagra")
    val = 0
else:
    print("Nu a aparut nici o eroare")
finally:
    print("Orice ar fi o sa se afiseze")

print("Dupa exceptie")
print(val)