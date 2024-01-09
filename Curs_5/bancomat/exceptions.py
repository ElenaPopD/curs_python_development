class Bancomat:
    def __init__(self, sold=1000):
        self.client = None
        self.sold = sold

    def autentificare(self, Client):
        self.client = Client

    def retragere_numarar(self):
        pass

    def interogare_sold(self):
        pass


class BancomatException(Exception):
    pass


class BancomatFaraBani(BancomatException):
    pass


class FonduriInsuficiente(BancomatException):
    pass


class PinGresit(BancomatException):
    pass
