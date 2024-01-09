board = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]
#  board[0]0] == board[1][1] == board[2][2] diagonala 
def check_winner():
    for row in board:
        if row.count("X") == 3 or row.count("O")==3:
            return True
    return False

def write(value, x, y):
    board[x][y] = value 

def get_coordonates():
    x = int(input(" dati x "))
    y = int(input(" dati y "))
    return(x,y)

def print_board():
    print("tabla arata asa: ")
    for row in board:
        for column in row:
          if column is None:
            print(" ", end="|")
          else:
            print(column, end ="|")
        print()


player = "X"
while True:
    print_board()
    print("Player", player)
    x,y = get_coordonates()
    write(player, x, y)
    print_board()

    if check_winner():
        print(f"Castigatorul este {player}")
        break
    
    if player == "X":
        player = "0"
    else:
        player = "X"