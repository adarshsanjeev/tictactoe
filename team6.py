#!/bin/python2.7

import random

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

    def get_empty_out_of(self, board, allowed, block):
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
            cells = self.get_empty_out_of(board, allowed, block)
        return cells
    
    def heuristic(self, board, block, new_move, flag):
        return random.randrange(-100, 100)

    def dfs_best_move(self, board, block, old_move, flag):
	blocks_allowed  = self.get_allowed_blocks(old_move, block)
        cells = self.get_empty_out_of(board, blocks_allowed, block)
        move_dict = {}

        # CASE FOR MAX DEPTH OR TERMINAL 
        # APPLY HEURISTIC
        for move in cells:
            move_dict[move] = self.heuristic(board, block, move, flag)
        k=list(move_dict.keys())
        v=list(move_dict.values())
        return k[v.index(max(v))]
    

    def move(self, board, block, old_move, flag):
        # HARDCODE INITAL GAME MOVEMENTS HERE

	return self.dfs_best_move(board, block, old_move, flag)
