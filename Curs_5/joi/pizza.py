class Pizza:
    def __init__(self):
        self.ingredients = ["cheese"]

    def make(self):
        print(self.ingredients)

    def add_ananas(self):
        self.ingredients.append("ananas naspa")

class AnanasMixin:

    def add_ananas(self):
        self.ingredients.append("ananas")

class SalamMixin:

    def add_salam(self):
        self.ingredients.append("salam")


class AndreiPizza(Pizza):
    pass

class ValentinPizza(Pizza, AnanasMixin):

    def make(self):
        self.add_ananas()
        super().make()

class AdrianPizza(AnanasMixin, Pizza):
    
     def make(self):
        self.add_salam()
        self.add_ananas()
        super().make()


pizza1 = AndreiPizza()
pizza1.make()

pizza2 = ValentinPizza()
pizza2.make()

pizza3 = AdrianPizza()
pizza3.make()




