#!/bin/python2.7

from team6 import Player6
pl6 = Player6()
pl6.myflag = 'x'

dicte = {
    0:'-',
    1:'x',
    2:'o'
}

board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

block = [0, 0, 0, 0, 0, 0, 0, 0, 0]

game_board = [    
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

print "{", 

while board[2][2] != 3:
    for i in range(len(board)):
        for j in range(len(board[i])):
            game_board[i][j] = dicte[board[i][j]]
    block = ['-'] * 9
    pl6.check_block_win(game_board, block, (0, 0), 'x')
    value = pl6.evaluate_block(0, game_board, 'x', 'o')
    print "'", pl6.make_block_str(game_board, 0), "'", ":", value, ",",

    board[0][0] += 1

    if board[0][0] == 3:
        board[0][0] = 0
        board[0][1] += 1

    if board[0][1] == 3:
        board[0][1] = 0
        board[0][2] += 1

    if board[0][2] == 3:
        board[0][2] = 0
        board[1][0] += 1

    if board[1][0] == 3:
        board[1][0] = 0
        board[1][1] += 1

    if board[1][1] == 3:
        board[1][1] = 0
        board[1][2] += 1

    if board[1][2] == 3:
        board[1][2] = 0
        board[2][0] += 1

    if board[2][0] == 3:
        board[2][0] = 0
        board[2][1] += 1

    if board[2][1] == 3:
        board[2][1] = 0
        board[2][2] += 1

print '}'

