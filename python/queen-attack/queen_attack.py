#create two functions, to display a board with two queens on it,
#and to answer if they can attack each other

def board(white,black):
    if not valid_coords(white,black):
        raise ValueError('Invalid Coordinates')
    #create an empty chessboard
    chess_board = [['_']*8 for _ in range(8)]
    #and populate with markers for the two queens
    chess_board[white[0]][white[1]] = 'W'
    chess_board[black[0]][black[1]] = 'B'
    return [''.join(line) for line in chess_board]

def can_attack(white,black):
    if not valid_coords(white,black):
        raise ValueError('Invalid Coordinates')
    #queens can attack if they share a row, column or diagonal
    row = white[0] == black[0]
    col = white[1] == black[1]
    diag = abs(white[0] - black[0]) == abs(white[1] - black[1])
    return row or col or diag

def valid_coords(x,y):
    #check the queens aren't on the same square
    ne = x != y
    #check the queens are on the board
    bounds = min(x) >= 0 and max(x) < 8 and min(y) >= 0 and max(y) < 8
    return ne and bounds
