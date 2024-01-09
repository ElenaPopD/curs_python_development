from Rock_paper_cod import hartie, piatra, foarfeca, runda_joc

def test_egalitate_runda():
    assert runda_joc(hartie, hartie) == "Egalitate"
    assert runda_joc(piatra, piatra) == "Egalitate"
    assert runda_joc(foarfeca, foarfeca) == "Egalitate"

def test_victorie_jucator1_runda():
    assert runda_joc(hartie, piatra) == "Jucatorul 1 castiga"
    assert runda_joc(foarfeca, hartie) == "Jucatorul 1 castiga"
    assert runda_joc(piatra, foarfeca) == "Jucatorul 1 castiga"

def test_victorie_jucator2_runda():
    assert runda_joc(piatra, hartie) == "Jucatorul 2 castiga"
    assert runda_joc(hartie, foarfeca) == "Jucatorul 2 castiga"
    assert runda_joc(foarfeca, piatra) == "Jucatorul 2 castiga"