#!/bin/python2.7

import random
import copy

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

    def check_block_win(self, board, block, move, flag):
        base = ((move[0]/3)*3, (move[1]/3)*3)
        block_id = base[0] + base[1]/3
        #ROWS
        for i in range(3):
            if board[base[0]+i][base[1]] == board[base[0]+i][base[1]+1] == board[base[0]+i][base[1]+2] == flag:
                block[block_id] = flag
                return True
        #COLS
        for i in range(3):
            if board[base[0]][base[1]+i] == board[base[0]+1][base[1]+i] == board[base[0]+2][base[1]+i] == flag:
                block[block_id] = flag
                return True
        #DIAG
        if board[base[0]][base[1]] == board[base[0]+1][base[1]+1] == board[base[0]+2][base[1]+2] == flag:
            block[block_id] = flag
            return True
        if board[base[0]+2][base[1]] == board[base[0]+1][base[1]+i] == board[base[0]][base[1]+2] == flag:
            block[block_id] = flag
            return True
        return False
    
    def heuristic(self, board, block, new_move, flag):
        # THIS FUNCTION, SHIVIN
        return random.randrange(-100, 100)

    def apply_move(self, board, block, move, flag):
        board[move[0]][move[1]] = flag
        # Update block variable
        self.check_block_win(board, block, move, flag)

    def check_terminal_state(self, board, block):
        # ROWS
        for i in range(3):
            if block[3*i] == block[3*i+1] == block[3*i+2] != '-':
                return block[i]
        # COLS
        for i in range(3):
            if block[i] == block[i+3] == block[i+6] != '-':
                return block[i]
        # DIAG
        if block[0] == block[4] == block[8] != '-' or block[2] == block[4] == block[8] != '-':
                return block[i]
        # DRAW
        if '-' not in block:
            return 'D'
        return '-'

    MAX_DEPTH = 1
    flag_alternate = {'x':'o', 'o':'x'}

    def dfs_best_move(self, board, block, old_move, flag, depth):
        # Get available blocks
	blocks_allowed  = self.get_allowed_blocks(old_move, block)
        cells = self.get_empty_out_of(board, blocks_allowed, block)
        # Process each in DFS
        move_dict = {}
        for move in cells:
            # Make temporary instance of the board
            temp_board = copy.deepcopy(board)
            temp_block = copy.deepcopy(block)
            # Apply the current move to the instance
            self.apply_move(temp_board, temp_block, move, flag)
            # Check if terminal
            winner = self.check_terminal_state(temp_board, temp_block)
            # If end node, apply heuristic, else, apply recursion
            if winner == '-' or depth+1 >= self.MAX_DEPTH:
                move_dict[move] = self.heuristic(temp_board, temp_block, move, flag)
            else:
                m, v = self.dfs_best_move(temp_board, temp_block, move, self.flag_alternate[flag], depth+1)
                move_dict[move] = v
        # Return maximum val
        k=list(move_dict.keys())
        v=list(move_dict.values())
        # Minimax
        if depth%2 == 0:
            return k[v.index(max(v))], v.index(max(v))
        else:
            return k[v.index(min(v))], v.index(min(v))
    
    def move(self, board, block, old_move, flag):
        # TODO HARDCODE INITAL GAME MOVEMENTS HERE

        # V = value
        m, v = self.dfs_best_move(board, block, old_move, flag, 0)
	return m

