def genereaza_numere_pare(limita):
    numar = 0
    while numar <= limita:
        yield numar
        numar += 2
        
for numar_par in genereaza_numere_pare(100):
    print(numar_par)