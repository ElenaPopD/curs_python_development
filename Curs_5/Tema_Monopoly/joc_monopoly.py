# from monopoly import Jucator
# from itertools import cycle
# from monopoly import Teren, Start, Gara, Utilitati, Inchisoare

# andrei=Jucator(nume="Andrei")
# florin = Jucator(nume="Florin")
# sabin = Jucator(nume = "Sabin")

# jucatori = [andrei, florin, sabin]

# masa = [Start(),
#         Teren("Timisoara"), Teren("Lugoj"), Teren("Turda"), 
#         Gara("De Nord"),Gara("De Sud"),
#         Inchisoare()]

# def last_man_standing(jucatori):
#     castigator =  [jucator for jucator in jucatori if jucator.sold > 0]
#     if len(castigator) == 1:
#         return castigator[0]

# def pozitie_finala(jucator, pozitii):
#     cycle_masa = cycle(masa) # 0
#     # jucator.pozitie # 1
#     for _ in range(jucator.pozitie):
#         next(cycle_masa)

#     next(cycle_masa)

#     for _ in range(pozitii):
#         element = next(cycle_masa)

#     return masa.index(element)

# # main()

# runde = 0
# for jucator in cycle(jucatori):
#     runde += 1
#     if jucator.sold <=0:
#         continue
#     zar_jucator = jucator.da_cu_zarul()
#     print(f"{jucator} a dat {zar_jucator}")
#     pozitie = pozitie_finala(jucator, zar_jucator)
#     jucator.pozitie = pozitie
#     print(jucator, jucator.pozitie, masa[jucator.pozitie])
#     casuta_curent = masa[jucator.pozitie]
#     casuta_curent.visit(jucator) 
#     winner = last_man_standing(jucatori)
#     if winner is not None:
#         print(f" Rezultat: {winner} a castigat! dupa {runde}  runde ")
#         break
    # if runde == 10:
    #     break   
    
    
from monopoly import Jucator, Teren, Start, Gara, Utilitati, Inchisoare
from itertools import cycle

# Inițializarea jucătorilor
andrei = Jucator(nume="Andrei")
florin = Jucator(nume="Florin")
sabin = Jucator(nume="Sabin")
jucatori = [andrei, florin, sabin]

# Crearea tabloului de joc
masa = [Start(),
        Teren("Timisoara"), Teren("Lugoj"), Teren("Turda"), Teren("București"),
        Gara("De Nord"), Gara("De Sud"),
        Utilitati("Apa"), Utilitati("Electricitate"), Utilitati("Gaz"),
        Inchisoare()]

# Funcția pentru determinarea câștigătorului
def last_man_standing(jucatori):
    castigator = [jucator for jucator in jucatori if jucator.sold > 0]
    if len(castigator) == 1:
        return castigator[0]

# Funcția pentru determinarea poziției finale
def pozitie_finala(jucator, pozitii):
    cycle_masa = cycle(masa)
    for _ in range(jucator.pozitie):
        next(cycle_masa)
    next(cycle_masa)  # Sari peste poziția curentă

    for _ in range(pozitii):
        element = next(cycle_masa)

    return masa.index(element)

# Bucla principală de joc
runde = 0
for jucator in cycle(jucatori):
    runde += 1
    if jucator.sold <= 0 or jucator.runde_in_inchisoare > 0:
        if jucator.runde_in_inchisoare > 0:
            jucator.runde_in_inchisoare -= 1
        continue

    zar_jucator = jucator.da_cu_zarul()
    print(f"{jucator} a dat {zar_jucator}")
    pozitie = pozitie_finala(jucator, zar_jucator)
    jucator.pozitie = pozitie
    print(jucator, jucator.pozitie, masa[jucator.pozitie])
    casuta_curent = masa[jucator.pozitie]
    casuta_curent.visit(jucator)
    
    winner = last_man_standing(jucatori)
    if winner:
        print(f"Rezultat: {winner} a castigat! dupa {runde} runde")
        break
    

    
    
    
    

