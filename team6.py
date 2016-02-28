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
        adjecent = copy.copy(self.adjecence_dict[new_block])
        adjecent = filter(lambda x: block[x] == '-', adjecent)
        if adjecent == []:
            adjecent = [i for i in range(9)]            
            adjecent = filter(lambda x: block[x] == '-', adjecent)
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
        return cells

    def print_board(self, board, block):
        for i in range(9):
            if i%3 == 0:
                print
            print 
            for j in range(9):
                if j%3 == 0:
                    print "   ",
                print board[i][j]," ",
        print "\n", block

    def check_block_win(self, board, block, move, flag):
        base = ((move[0]/3)*3, (move[1]/3)*3)
        block_id = base[0] + base[1]/3
        # print move, flag
        # print base, block_id
        # print "BEFORE"
        # self.print_board(board, block)
        #ROWS
        for i in range(base[0], base[0]+3):
            if board[i][base[1]] == board[i][base[1]+1] == board[i][base[1]+2] == flag:
                block[block_id] = flag
        #COLS
        for i in range(base[1], base[1]+3):
            if board[base[0]][i] == board[base[0]+1][i] == board[base[0]+2][i] == flag:
                block[block_id] = flag
        #DIAG
        if board[base[0]][base[1]] == board[base[0]+1][base[1]+1] == board[base[0]+2][base[1]+2] == flag:
            block[block_id] = flag
        if board[base[0]+2][base[1]] == board[base[0]+1][base[1]+1] == board[base[0]][base[1]+2] == flag:
            block[block_id] = flag
            
        for i in range(base[0], base[0]+3):
            for j in range(base[1], base[1]+3):
                if board[i][j] == '-':
                    pass
            else:
                block[block_id] = 'D'
    
    def heuristic(self, board, block, new_move, flag):
        # THIS FUNCTION, SHIVIN
        return random.randrange(-100, 100)

    def apply_move(self, board, block, move, flag):
        board[move[0]][move[1]] = flag
        # Update block variable
        self.check_block_win(board, block, move, flag)

    def check_terminal_state(self, board, block):
        if '-' in block:
            return False
        else:
            return True

    MAX_DEPTH = 2
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
            # If end node, apply heuristic, else, apply recursion
            if self.check_terminal_state(temp_board, temp_block) is True or depth+1 >= self.MAX_DEPTH:
                move_dict[move] = self.heuristic(temp_board, temp_block, move, flag)
            else:
                m, v = self.dfs_best_move(temp_board, temp_block, move, self.flag_alternate[flag], depth+1)
                move_dict[move] = v
        # Return maximum val
            k=list(move_dict.keys())
            v=list(move_dict.values())
        try:
            v.index(max(v))
        except ValueError:
            print "HELLO DARKNESS, MY OLD FRIEND"
            raise
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

