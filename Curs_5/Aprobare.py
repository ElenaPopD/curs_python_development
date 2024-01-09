from Chain import Chain


class Manager(Chain):
    max_amount = 1000


class Director(Chain):
    max_amount = 10000


class CEO(Chain):
    def can_handle(self, request):
        return True


marius = Manager('Marius')
valentin = Director('Valentin')
gogu = CEO('Gogu')
marius.set_next(valentin)
valentin.set_next(gogu)
marius.handle(11000)
