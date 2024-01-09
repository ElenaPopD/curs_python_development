from monopoly import Jucator, Start, Teren, Inchisoare, Gara
from joc_monopoly import pozitie_finala
from unittest import mock

def test_zar():
    george = Jucator("George")
    with mock.patch('monopoly.randrange') as randrange:
        randrange.return_value = 12
        valoare = george.da_cu_zarul()
        assert valoare == 12


def test_pozitie_finala():
    george = Jucator("George")
    masa = [
        Start(),
        Teren("Ceva", judet="Cluj"), Teren("Altceva",  judet="Cluj"), Teren("1",  judet="Cluj"),
        Inchisoare()
    ]
    #masa = range(5)
    pozitie = pozitie_finala(masa, george, 10)
    assert pozitie == 0


def test_cumparare_teren():
    george = Jucator("George")
    teren = Teren("Cluj", judet="Cluj", pret=1000)
    teren.visit(george)
    assert teren.proprietar == george

def test_cumparare_modifica_sold():
    george = Jucator("George", sold=1500)
    teren = Teren("Cluj",  judet="Cluj", pret=1000)
    teren.visit(george)
    assert george.sold == 500

def test_cumparare_teren_fonduri_insuficiente():
    george = Jucator("George", sold=500)
    teren = Teren("Cluj", judet="Cluj", pret=1000)
    teren.visit(george)
    assert teren.proprietar is None

def test_plata_chirie():
    george = Jucator("George", sold=1500)
    ionel = Jucator("Ionel", sold=500)
    teren = Teren("Cluj", judet="Cluj", pret=1000, chirie=100)
    teren.visit(george)
    # assert teren.proprietar == george
    # assert george.sold == 500
    teren.visit(ionel)
    assert ionel.sold == 400


def test_are_tot_cartierul():
    jucator = Jucator("George", sold=15000)
    cartier = [
        Teren("Timisoara", judet="Timis"),
        Teren("Lugoj", judet="Timis"),
        Teren("Faget", judet="Timis")
    ]
    for teren in cartier:
        teren.visit(jucator)
    
    assert jucator.are_tot_judetul("Timis") is True

def test_cartier_lipseste_una():
    jucator = Jucator("George", sold=10000)
    cartier = [
        Teren("Timisoara", judet="Timis"),
        Teren("Lugoj", judet="Timis"),
        Gara("Nord")
    ]
    for teren in cartier:
        teren.visit(jucator)
    
    assert jucator.are_tot_judetul("Timis") is False


def test_cartier_cu_2_terenuri():
    jucator = Jucator("George", sold=10000)
    cartier = [
        Teren("Timisoara", judet="Timis", terenuri_in_judet=2),
        Teren("Lugoj", judet="Timis", terenuri_in_judet=2),
        Gara("Nord")
    ]
    for teren in cartier:
        teren.visit(jucator)
    
    assert jucator.are_tot_judetul("Timis") is True


def test_construieste_o_casuta():
    jucator = Jucator("George", sold=15000)
    cartier = [
        Teren("Timisoara", judet="Timis"),
        Teren("Lugoj", judet="Timis"),
        Teren("Faget", judet="Timis")
    ]
    for teren in cartier:
        teren.visit(jucator)

    teren.visit(jucator)

    assert teren.casute == 1

def test_construieste_o_casuta():
    jucator = Jucator("George", sold=15000)
    cartier = [
        Teren("Timisoara", judet="Timis"),
        Teren("Lugoj", judet="Timis"),
        Teren("Faget", judet="Timis")
    ]
    for teren in cartier:
        teren.visit(jucator)
    teren.visit(jucator)
    assert teren.casute  == 1


def test_chiria_creste_cu_o_casuta():
    jucator = Jucator("George", sold=15000)
    cartier = [
        Teren("Timisoara", judet="Timis"),
        Teren("Lugoj", judet="Timis"),
        Teren("Faget", judet="Timis", chirie=100)
    ]
    for teren in cartier:
        teren.visit(jucator)
    teren.visit(jucator) # construieste casa
    assert teren.chirie == 105


def test_chiria_creste_cu_casutele():
    jucator = Jucator("George", sold=15000)
    cartier = [
        Teren("Timisoara", judet="Timis"),
        Teren("Lugoj", judet="Timis"),
        Teren("Faget", judet="Timis", chirie=100)
    ]
    for teren in cartier:
        teren.visit(jucator)
    teren.visit(jucator) # construieste casa
    teren.visit(jucator) # construieste a doua casa
    assert teren.chirie == 200



