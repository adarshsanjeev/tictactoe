#!/bin/python2.7

class Player6:
    	
    def __init__(self):
	pass
    
    def move(self, board, block, old_move, flag):
	blocks_allowed  = determine_blocks_allowed(old_move, temp_block)
	cells = get_empty_out_of(temp_board, blocks_allowed,temp_block)
	return cells[random.randrange(len(cells))]

