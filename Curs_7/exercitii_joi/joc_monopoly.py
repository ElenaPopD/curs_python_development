from monopoly import Jucator
from itertools import cycle
from monopoly import Teren, Start, Gara, Utilitati, Inchisoare

andrei=Jucator(nume="Andrei")
florin = Jucator(nume="Florin")
sabin = Jucator(nume = "Sabin")

jucatori = [andrei, florin, sabin]

masa = [Start(),
        Teren("Timisoara", judet="Timis"), Teren("Lugoj", judet="Timis"), Teren("Faget", judet="Timis"), 
        Gara("De Nord"),
        Teren("Cluj-Napoca", judet="Cluj"), Teren("Turda", judet="Cluj"), Teren("Dej", judet="Cluj"),
        Gara("De Sud"),
        Teren("Braila", judet="Braila", terenuri_in_judet=1),
        Inchisoare()
    ]

def last_man_standing(jucatori: list) -> Jucator:
    castigator =  [jucator for jucator in jucatori if jucator.sold > 0]
    if len(castigator) == 1:
        return castigator[0]

def pozitie_finala(masa: list, jucator: Jucator, pozitii: int) -> int:
    cycle_masa = cycle(masa) # 0
    # jucator.pozitie # 1
    for _ in range(jucator.pozitie):
        next(cycle_masa)

    next(cycle_masa)

    for _ in range(pozitii):
        element = next(cycle_masa)

    return masa.index(element)

# main()

runde = 0
for jucator in cycle(jucatori):
    runde += 1
    if jucator.sold <=0:
        continue
    zar_jucator = jucator.da_cu_zarul()
    print(f"{jucator} a dat {zar_jucator}")
    pozitie = pozitie_finala(masa, jucator, zar_jucator)
    jucator.pozitie = pozitie
    print(jucator, jucator.pozitie, masa[jucator.pozitie])
    casuta_curent = masa[jucator.pozitie]
    casuta_curent.visit(jucator) 
    winner = last_man_standing(jucatori)
    if winner is not None:
        print(f" Rezultat: {winner} a castigat! dupa {runde}  runde ")
        break
    # if runde == 10:
    #     break   
    
    

    

    
    
    
    

