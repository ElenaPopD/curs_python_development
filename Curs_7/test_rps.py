from rps import rps

import pytest



@pytest.mark.parametrize("player1,player2", (
        ("Hartie", "Hartie"),
        ("Piatra", "Piatra"),
        ("Foarfeca", "Foarfeca")
))
def test_remiza(player1, player2):
    assert rps(player1, player2) == 0

@pytest.mark.parametrize("player1,player2", (
        ("Hartie", "Piatra"),
        ("Foarfeca", "Hartie"),
        ("Piatra", "Foarfeca")
))
def test_player1_wins(player1, player2):
    assert rps(player1, player2) == 1


@pytest.mark.parametrize("player1,player2", (
        ("Piatra", "Hartie"),
        ("Hartie", "Foarfeca"),
        ("Foarfeca", "Piatra")
))
def test_player2_wins(player1, player2):
    assert rps(player1, player2) == 2