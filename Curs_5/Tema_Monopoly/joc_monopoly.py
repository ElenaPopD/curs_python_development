
from monopoly import Jucator, Teren, Start, Gara, Utilitati, Inchisoare
from itertools import cycle


andrei = Jucator(nume="Andrei")
florin = Jucator(nume="Florin")
sabin = Jucator(nume="Sabin")
jucatori = [andrei, florin, sabin]


masa = [Start(),
        Teren("Timisoara"), Teren("Lugoj"), Teren("Turda"), Teren("București"),
        Gara("De Nord"), Gara("De Sud"),
        Utilitati("Apa"), Utilitati("Electricitate"), Utilitati("Gaz"),
        Inchisoare()]

# Functia pentru determinarea winner
def last_man_standing(jucatori):
    castigator = [jucator for jucator in jucatori if jucator.sold > 0]
    if len(castigator) == 1:
        return castigator[0]

# Functia pentru determinarea pozitiei finale
def pozitie_finala(jucator, pozitii):
    cycle_masa = cycle(masa)
    for _ in range(jucator.pozitie):
        next(cycle_masa)
    next(cycle_masa)  # Sari peste pozitia curenta

    for _ in range(pozitii):
        element = next(cycle_masa)

    return masa.index(element)

# Bucla principala de joc
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
    

    
    
    
    

