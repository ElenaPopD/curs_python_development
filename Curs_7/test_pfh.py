from pfh import castigator, alegere
from pfh import hartie, piatra, foarfeca

import pytest


@pytest.mark.parametrize("player1,player2", (
        (hartie, hartie),
        (piatra, piatra),
        (foarfeca, foarfeca)
))
def test_remiza(player1, player2):
    assert castigator(player1, player2) == None

@pytest.mark.parametrize("player1,player2", (
        (hartie, piatra),
        (foarfeca, hartie),
        (piatra, foarfeca)
))
def test_player1_wins(player1, player2):
    assert castigator(player1, player2) == 0


@pytest.mark.parametrize("player1,player2", (
        (piatra, hartie),
        (hartie, foarfeca),
        (foarfeca, piatra)
))
def test_player2_wins(player1, player2):
    assert castigator(player1, player2) == 1


def test_alegere():
    
    alegere("Dorel") == 3