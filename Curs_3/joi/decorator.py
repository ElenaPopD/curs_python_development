def decorator(func):
    def inner(*args, **kwargs):
        print("Inainte")
        func(*args, **kwargs)
        print("Dupa")
    return inner

@decorator
def salut(nume):
    print(f"Salut {nume}!")

@decorator
def salut_tare(nume, param2=True):
    print(f"SALUT {nume}!")

salut("Georgel")
salut_tare("George")