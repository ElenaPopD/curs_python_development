from xo import check_winner

def test_linie():
    board = [
        ["X", "X", "X"],
        [None, None, None],
        [None, None, None]
    ]
    assert check_winner(board) == True

def test_castiga_0_linie():
    board = [
        ["O", "O", "O"],
        [None, None, None],
        [None, None, None]
    ]
    assert check_winner(board) == True


def test_castiga_x_linie_2():
    board = [
        [None, None, None],
        ["X", "X", "X"],
        [None, None, None]
    ]
    assert check_winner(board) == True

def test_nici_un_castigator():
    board = [
        [None, None, None],
        [None, "X", None],
        [None, None, None]
    ]
    assert check_winner(board) == False

