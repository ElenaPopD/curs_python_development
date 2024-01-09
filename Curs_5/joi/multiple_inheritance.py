class Mama:
    atribut1 = "Unu"

    def metoda(self):
        print("Sunt in Mama")

class Tata:
    atribut1 = "Tata"
    atribut2 = "Doi"

    def metoda(self):
        print("Sunt in Tata")

class Copil(Mama, Tata):
    pass

class CopilTata(Tata, Mama):
    pass

copil = Copil()
print(copil.atribut1)
print(copil.atribut2)
print(copil.metoda())
print(Copil.__mro__)
print(CopilTata.__mro__)
copiltata = CopilTata()
print(copiltata.metoda())