# Given a list of strings representing a minesweeper board,
# correctly populate the spaces with the number of adjacent mines
# raise a value error if the board is malformed, or contains invalid characters

import re

def validate_input(board_list):
    #start by checking all lines are of equal length
    if any(len(elem) != len(board_list[0]) for elem in board_list):
        return False
    #check the board is correctly formatted
    bound = re.compile(r'^\+\-*\+$')
    middle = re.compile(r'^\|[* ]*\|$')
    start = re.match(bound,board_list[0])
    end = re.match(bound,board_list[-1])
    mid = all(re.match(middle,elem) for elem in board_list[1:-1])
    return start and end and mid

def get_neighbours(x,y):
    #return a list of coordinates that neighbour x and y
    return [(x-1, y-1), (x, y-1), (x+1, y-1),
            (x-1, y), (x+1, y),
            (x-1, y+1), (x, y+1), (x+1, y+1)]

def board(board_list):
    #check we have a valid board
    if not validate_input(board_list):
        raise ValueError('Malformed Board')
    #convert the strings into a list of chars, so we can update the board
    #with the mine counts
    field = [map(str,line) for line in board_list]
    for row, line in enumerate(field):
        for col, elem in enumerate(line):
            #only consider empty 'squares'
            if elem != ' ': continue
            neighbours = [field[x][y] for x, y in get_neighbours(row,col)]
            mine_count = neighbours.count('*')
            #'squares' with no adjacent mines are left blank
            field[row][col] = str(mine_count) if mine_count > 0 else ' '
    return [''.join(line) for line in field]
