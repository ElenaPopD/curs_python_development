cuvant = "ciocolata"
vieti = 3

litere_ghicite = set()
set_cuvant = set(cuvant)
while vieti > 0:
    # Afisez litere ghicite pana acum
    for litera_cuvant in cuvant:
        if litera_cuvant in litere_ghicite:
            print(litera_cuvant, end="")
        else:
            print("*", end="")
    print("")

    litera = input("Dati o litera:")
    if litera in set_cuvant:
        litere_ghicite.add(litera)
        if set_cuvant == litere_ghicite:
            print("Ai castigat")
            break
        print("Ai ghicit")
    else:
        vieti = vieti - 1
        print("Ai gresit")
else:
    print("Ai ramas fara vieti")

