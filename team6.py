#!/bin/python2.7

import random
import copy



class Player6:
    def __init__(self):
        pass
    
    WIN = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    mapping = {'x':1,'-':0,'o':-1}
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
                return
        #COLS
        for i in range(base[1], base[1]+3):
            if board[base[0]][i] == board[base[0]+1][i] == board[base[0]+2][i] == flag:
                block[block_id] = flag
                return
        #DIAG
        if board[base[0]][base[1]] == board[base[0]+1][base[1]+1] == board[base[0]+2][base[1]+2] == flag:
            block[block_id] = flag
            return
        if board[base[0]+2][base[1]] == board[base[0]+1][base[1]+1] == board[base[0]][base[1]+2] == flag:
            block[block_id] = flag
            return
            
        for i in range(base[0], base[0]+3):
            for j in range(base[1], base[1]+3):
                if board[i][j] == '-':
                    return
        block[block_id] = 'D'
    
    def heuristic(self, board, block, new_move, flag):
        # THIS FUNCTION, SHIVIN
        return self.evaluate_board(board,block,flag,self.flag_alternate[flag])
        #return random.randrange(-100, 100)
    
        self.mapping[flag]=1
        self.mapping[self.flag_alternate[flag]]=-1


    def evaluate_block(self,block_id,board,flag1,flag2):
        
        self.mapping[flag1]=1
        self.mapping[self.mapping[flag2]]=-1
        
        power = 0
        base = ((block_id//3)*3, (block_id%3)*3)
        block_id = base[0] + base[1]/3
        val = 0
        #ROWS
        for i in range(3):
            val = 0
            for j in range(3):
                val = val + self.mapping[board[base[0]+i][base[1]+j]]
            if val > 0 :
                power = power + pow(10,val)
            elif val < 0 :
                power = power - pow(10,-1*val)
    
        #COLS
        for j in range(3):
            val = 0
            for i in range(3):
                val = val + self.mapping[board[base[0]+i][base[1]+j]]
            if val > 0 :
                power = power + pow(10,val)
            elif val < 0 :
                power = power - pow(10,-1*val)
        
        val=0
        for i in range(3):
            val = val + self.mapping[board[base[0]+i][base[1]+i]]
        if val > 0 :
            power = power + pow(10,val)
        elif val < 0 :
            power = power - pow(10,-1*val)
    
        val = 0
        for i in range(3):
            val = val + self.mapping[board[base[0]+i][base[1]+2-i]]
        if val > 0 :
            power = power + pow(10,val)
        elif val < 0 :
            power = power - pow(10,-1*val)
        
        return power
    

    def evaluate_board(self,board,blocks,flag1,flag2):
        sum = 0
        for line in self.WIN:
            val = 0
            for cell in line:
                if(blocks[cell]==flag1):
                    val+=1
                elif(blocks[cell]==flag2):
                    val-=1
            if(val>0):
                sum = sum + 10*pow(10,val)
            elif(val<0):
                sum = sum - 10*pow(10,-1*val)
        
        for i in range(9):
            sum = sum + self.evaluate_block(i,board,flag1,flag2)
        return sum 

    def apply_move(self, board, block, move, flag):
        board[move[0]][move[1]] = flag
        # Update block variable
        self.check_block_win(board, block, move, flag)

    def check_terminal_state(self, board, block):
        if '-' in block:
            return False
        else:
            return True

    MAX_DEPTH = 4
    flag_alternate = {'x':'o', 'o':'x'}

    def dfs_best_move(self, board, block, old_move, flag, depth, alpha, beta):
        # Get available blocks
	blocks_allowed  = self.get_allowed_blocks(old_move, block)

        # BASE HARDCODE
        if sum(1 for row in board for i in row if i == '-') > 73:
            for choice in blocks_allowed:
                base = ((choice/3)*3+1, (choice%3)*3+1)
                if board[base[0]][base[1]] == '-':
                    pass#                    return base, 0
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
                m, v = self.dfs_best_move(temp_board, temp_block, move, self.myflag, depth+1, alpha, beta)
                move_dict[move] = v
                if depth%2 == 0: #MAX NODE
                    node_val = max(list(move_dict.values()))
                    alpha = node_val
                    if beta is not None and beta <= alpha:
                        break
                else:            #MIN NODE
                    node_val = min(list(move_dict.values()))
                    beta = node_val
                    if alpha is not None and beta <= alpha:
                        break
        # Return maximum val
        # print depth, "###", old_move, move_dict
        k=list(move_dict.keys())
        v=list(move_dict.values())
        # Minimax
        if depth%2 == 0:
            return k[v.index(max(v))], max(v)
        else:
            return k[v.index(min(v))], min(v)

    def move(self, board, block, old_move, flag):
        # TODO HARDCODE INITAL GAME MOVEMENTS HERE
        # V = value
        print block
        self.myflag = flag
        m, v = self.dfs_best_move(board, block, old_move, flag, 0, None, None)
	return m

