class BunicMama:
    pass
class BunicaMama:
    pass

class Mama(BunicMama, BunicaMama):
    atribut1 = "Unu"

    def metoda(self):
        print("Sunt in Mama")

class BunicTata:
    pass
class BunicaTata:
    pass

class Tata(BunicTata, BunicaTata):
    atribut1 = "Tata"
    atribut2 = "Doi"

    def metoda(self):
        print("Sunt in Tata")

class Copil(Mama, Tata):
    pass

class CopilTata(Tata, Mama):
    pass

print(Copil.__mro__)
print(CopilTata.__mro__)

