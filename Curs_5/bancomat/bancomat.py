from exceptions import FonduriInsuficiente, BancomatFaraBani


class Client:
    def __init__(self, nume, sold_client=100):
        self.nume = nume
        self.sold_client = sold_client


class Bancomat:
    def __init__(self, sold=1000):
        self.client = None
        self.sold = sold

    def autentificare(self, client):
        self.client = client

    def retragere_numarar(self, suma_dorita):
        if suma_dorita > self.sold:
            raise BancomatFaraBani("Nu am ce sa iti dau")
        if suma_dorita > self.client.sold_client:
            raise FonduriInsuficiente("Nu ai bani")
        self.sold -= suma_dorita
        self.client.sold_client -= suma_dorita

        print(f"Ai retras suma de: {suma_dorita}")


    def interogare_sold(self):
        print(f' {self.client.nume}, soldul tau disponibil este: {self.client.sold_client}')


nicu = Client("Nicu", sold_client=1000)
gogu = Client("Gogu", sold_client=50)
ion = Client("Ion", sold_client=200)

atm = Bancomat(50)
atm.autentificare(ion)
atm.interogare_sold()

try:
    atm.retragere_numarar(100)
except BancomatFaraBani as e:
    print(e)
    atm.retragere_numarar(10)

atm.interogare_sold()
