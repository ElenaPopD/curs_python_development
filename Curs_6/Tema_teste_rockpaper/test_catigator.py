from Rock_paper_cod import piatra, foarfeca, hartie, castigator

def test_egalitate():
    assert castigator(hartie, hartie) == 0
    assert castigator(piatra, piatra) == 0
    assert castigator(foarfeca, foarfeca) == 0

def test_castigator_jucator1():
    assert castigator(hartie, piatra) == 1
    assert castigator(foarfeca, hartie) == 1
    assert castigator(piatra, foarfeca) == 1

def test_castigator_jucator2():
    assert castigator(piatra, hartie) == 2
    assert castigator(hartie, foarfeca) == 2
    assert castigator(foarfeca, piatra) == 2