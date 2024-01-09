board = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]

def check_winner(board):
    for row in board:
        if row.count("X") == 3 or row.count("O") == 3:
            return True
    return False