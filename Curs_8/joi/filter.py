numere = (x for x in range(20)) # genereaza cate un numar pe rand
# numere = [x for x in range(20)] # tine in memorie 20 de numere

numere_pare = (numar for numar in numere if numar % 2 == 0 )

numere_pare_filter = filter(lambda numar: numar % 2 == 0, range(20))
# 5 in numere_pare

for numar_par in numere_pare_filter:

    print(numar_par)

# avem_5 = (numar for numar in numere_pare if numar == 5 )

# for numar in numere_pare:
#     if 5 == numar:
#         break

# 5 in numere_pare
    
