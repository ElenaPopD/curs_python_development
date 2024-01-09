multiplier = 3

def inmultire(a, b):
    rezultat = a * b
    rezultat_final = rezultat * multiplier
    return rezultat_final

print(inmultire(2, 3))

def main_func(a, b):
    c = 10
    def inner_func():
        a = 50
        print(a + b + c + multiplier)
    inner_func()

main_func(2, 3)