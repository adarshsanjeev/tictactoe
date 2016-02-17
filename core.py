#!/bin/python2.7

class Player6:

    def __init__(self):
        pass

    adjecence_dict = {
        0: [1, 3],
        1: [0, 2],
        2: [1, 5],
        3: [0, 6],
        4: [4],
        5: [2, 8],
        6: [3, 7],
        7: [6, 8],
        8: [5, 7],
    }

    def get_allowed_blocks(self, old_move, block):
        if old_move == (-1, -1):
            return [i for i in range(9)]

        coordinate = (old_move[0]%3, old_move[1]%3)
        new_block = coordinate[0]*3 + coordinate[1]
        adjecent = self.adjecence_dict[new_block]
        for index, val in enumerate(adjecent):
            if block[val] != '-':
                adjecent[index] = -1
        adjecent = filter(lambda x: x != -1, adjecent)
        return adjecent
    
    def move(self, board, block, old_move, flag):
	blocks_allowed  = self.get_allowed_blocks(old_move, block)
        cells = get_empty_out_of(board, blocks_allowed, block)
	return cells[random.randrange(len(cells))]

