class PrintableMixin(object):

    def print(self):
        return self.__dict__

class OchiNegriMixin:
    def __init__(self):
        self.culoare_ochi = "Negru"


class Copil(PrintableMixin):

    def __init__(self, nume, virsta):
        super().__init__()
        self.nume = nume
        self.virsta = virsta

class Animal(PrintableMixin):
    pass


copil = Copil("Ionel", 10)
dict_copil = copil.print()
print(dict_copil)