hartie = 1
piatra = 2
foarfeca = 3

runde_input = 1

score = [0, 0]


def castigator(player1, player2):
    if player1 == player2:
        return None
    elif (player1, player2) in [(hartie, piatra), (foarfeca, hartie), (piatra, foarfeca)]:
        return 0
    else:
        return 1


def alegere(Jucator):
    choice = input(f"{Jucator} Alege: Hartie - 1, Piatra - 2, Foarfeca - 3--->")
    return int(choice)


def main():
    player1 = alegere("Jucator 1 :")
    player2 = alegere("Jucator 2 :")
    winner = castigator(player1, player2)
    if winner:
        score[winner] += 1
    return score


def runde(nr_runde):
    if nr_runde in (3, 5):
        return nr_runde
    else:
        nr_runde = int(input('Ati gresit numarul de runde selectat! Introduceti din nou, 3 sau 5 runde: '))
        return nr_runde


def check_score():
    if sum(score) == int(nr_runde/2)+1 and score[0] != score[1]:
        return False
    else:
        return True



if __name__ == "__main__":

    nr_runde = int(input('Introduceti numarul de runde, 3 sau 5: '))
    runde(nr_runde)
    while check_score() is True and runde_input <= nr_runde:
        print(f'Runda {runde_input} din {nr_runde}:')
        main()
        runde_input += 1
        print(f'Rezultat:\n Jucator 1: {score[0]}\n Jucator 2: {score[1]}')
        print('\n')
        check_score()

    if score[0] == score[1]:
        print("Remiza")
    elif score[0] > score[1]:
        print('Jucatorul 1 a castigat partida!')
    else:
        print('Jucatorul 2 a castigat partida!')
