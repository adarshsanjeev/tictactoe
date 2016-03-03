#!/bin/python2.7

dicte = {
    0:'-',
    1:'x',
    2:'o'
}

board = 9*[0]

print "{",
while board[-1] != 2:
    output = [dicte[i] for i in board]
    print "'"+"".join(output)+ "',",
    board[0] += 1
    for index, val in enumerate(board):
        if val > 2:
            board[index] %= 3
            if index != len(board)-1:
                board[index+1] += 1
    
print "}"

