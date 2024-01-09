def rps(player1, player2):
    if player1 == player2:
        return 0
    if (player1, player2) in (
        ("Hartie", "Piatra"),
        ("Foarfeca", "Hartie"),
        ("Piatra", "Foarfeca")
    ):
        return 1
    else:
        return 2

def main():
    input()