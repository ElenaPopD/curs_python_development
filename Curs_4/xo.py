board = [
    [11, 12, 13],
    [21, 22, 23],
    [31, 32, 33]
]

for rand in board:
    print(rand, type(rand))

# board[0][0] -> 11
# board[1][0] -> 21
# board[2][0] -> 31
# board[1][0] -> 12
# board[1][1] -> 22
# board[1][2] -> 32

for coloana in range(0,3):
    for rand in range(0,3):
        print(board[rand][coloana])

board[0][0] == board[1][1] == board[2][2] != None # diag 1
board[0][2] == board[1][1] == board[2][0] != None # diag 2
