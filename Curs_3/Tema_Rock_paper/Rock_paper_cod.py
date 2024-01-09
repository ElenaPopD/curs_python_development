# Constamtele
hartie = 1
piatra = 2
foarfeca = 3

# Functia castigator 
def castigator(player1, player2):
    if player1 == player2:
        return 0
    if (player1, player2) in [(hartie, piatra), (foarfeca, hartie), (piatra, foarfeca)]:
        return 1
    else:
        return 2

# Functia pentru a obtine alegerea unui jucator
def alegere(Jucator):
    choice = input(f"{Jucator} Alege: Hartie - 1, Piatra - 2, Foarfeca - 3 ---> ")
    return int(choice)

# Functia pentru a transforma alegerea numerica intr-un nume
def nume_alegere(alegere):
    if alegere == hartie:
        return "Hartie"
    elif alegere == piatra:
        return "Piatra"
    else:
        return "Foarfeca"

# functie care ruleaza o runda
def runda_joc(player1, player2):
    rezultat = castigator(player1, player2)
    if rezultat == 0:
        return "Egalitate"
    elif rezultat == 1:
        return "Jucatorul 1 castiga"
    else:
        return "Jucatorul 2 castiga"

# Functia principala
def main():
    scor_jucator1 = 0
    scor_jucator2 = 0
    
    numar_runde = int(input("Doriti un joc de 3 sau 5 runde? "))
    if numar_runde not in [3, 5]:
        print("Alegeti numarul de runde corect (3 sau 5).")
        return

    for runda in range(numar_runde):
        print(f"Runda {runda + 1}")
        player1 = alegere("Jucator 1:")
        player2 = alegere("Jucator 2:")
        rezultat_runda = runda_joc(player1, player2)
        print(rezultat_runda)

        if rezultat_runda == "Jucatorul 1 castiga":
            scor_jucator1 += 1
        elif rezultat_runda == "Jucatorul 2 castiga":
            scor_jucator2 += 1
        
        print(f"Jucatorul 1 a ales {nume_alegere(player1)} si Jucatorul 2 a ales {nume_alegere(player2)}")
        print(f"Scorul actual este: Jucator unu - {scor_jucator1}, Jucator doi - {scor_jucator2}\n")

    # Determinam castigatorul final
    if scor_jucator1 > scor_jucator2:
        print("Castigatorul meciului este Jucatorul 1!")
    elif scor_jucator1 < scor_jucator2:
        print("Castigatorul meciului este Jucatorul 2!")
    else:
        print("Meciul s-a terminat la egalitate!")

# main()

