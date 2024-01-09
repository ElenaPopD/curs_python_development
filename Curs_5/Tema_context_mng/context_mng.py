#definesc o clasa care implementeaza metodele __enter__ si __exit__ 
# in metoda __exit__,  adaug logica de tratament a exceptiilor

class MyContextManager:
    def __enter__(self):
        print("Initializarea resurselor.")
        self.resource = open('fisier.txt', 'w')
        return self.resource

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is KeyError or exc_type is IndexError:
            print(f"Exceptie prinsa: {exc_type.__name__}")
            return True
        print("Inchiderea resurselor.")
        self.resource.close()
        return False

# Utilizarea managerului de context
with MyContextManager() as fisier:
    fisier.write("Acesta este un test.")  # Scrie în fisier

    print("Operatiuni cu fisierul finalizate.")
