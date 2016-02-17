#!/bin/python2.7

class Player6:
    	
    def __init__(self):
	pass
    
    def move(self, board, block, old_move, flag):
	blocks_allowed  = determine_blocks_allowed(old_move, temp_block)
	cells = get_empty_out_of(temp_board, blocks_allowed,temp_block)
	return cells[random.randrange(len(cells))]


def get_empty_out_of(board, allowed, block):
    cells = []
    for val in allowed:
        row_val = (val//3)*3
        col_val = (val%3)*3
        for i in range(row_val, row_val+3):
            for j in range(col_val, col_val+3):
                if board[i][j] == '-':
                    cells.append((i, j))

    if cells == []:
        allowed = []
        for val in range(0, 9):
            if block[val] == '-':
                allowed.append(val)
        cells = get_empty_out_of(board, allowed, block)

    return cells
