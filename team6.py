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

    def make_block_str(self, board, block_number):
        x,y = self.get_block_coords(block_number)
        string = ""
        for i in xrange(x,x+3):
            for j in xrange(y,y+3):
                string += board[i][j]
        return string
    
    def get_block_coords(self,block_number):
        return {
            0 : (0, 0),
            1 : (0, 3),
            2 : (0, 6),
            3 : (3, 0),
            4 : (3, 3),
            5 : (3, 6),
            6 : (6, 0),
            7 : (6, 3),
            8 : (6, 6),
        }.get(block_number)


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
        #return random.randrange(-100, 100)
        self.mapping[flag]=1
        self.mapping[self.flag_alternate[flag]]=-1
        return self.evaluate_board(board,block,flag,self.flag_alternate[flag])

    def evaluate_block(self,block_id,board,flag1,flag2):
        
        self.mapping[flag1]=1
        self.mapping[flag2]=-1
        
        power = 0
        base = ((block_id//3)*3, (block_id%3)*3)
        block_id = base[0] + base[1]/3
        val = 0
        #ROWS
        for i in range(3):
            val = 0
            for j in range(3):
                val = val + self.mapping[board[base[0]+i][base[1]+j]]
            if(val>=2):
                power = power + val
            elif(val<=-2):
                power = power + val

    
        #COLS
        for j in range(3):
            val = 0
            for i in range(3):
                val = val + self.mapping[board[base[0]+i][base[1]+j]]
            if(val>=2):
                power = power + val
            if(val<=-2):
                power = power + val
        
        val=0
        for i in range(3):
            val = val + self.mapping[board[base[0]+i][base[1]+i]]
        if(val>=2):
            power = power + val
        if(val<=-2):
            power = power + val
    
        val = 0
        for i in range(3):
            val = val + self.mapping[board[base[0]+i][base[1]+2-i]]
        if(val>=2):
            power = power + val
        if(val<=-2):
            power = power + val
        
       
        if 1 or (board[base[0]+1][base[1]+1]==flag1):
            power = power + 2*self.mapping[board[base[0]+1][base[1]+1]]

        for i in [0,2]:
            for j in [0,2]:
                power = power + self.mapping[board[base[0]+1][base[1]+1]]

        
        val=0
        for i in range(base[0],base[0]+3):
            for j in range(base[1],base[1]+3):
                val = val+self.mapping[board[i][j]]
        
        if block_id == 4:
            val = val*2

        power = power + val
        return power
    

    def evaluate_board(self,board,blocks,flag1,flag2):
        sum = 0
        if(len(blocks)>2):
            sum = sum + 5
        for line in self.WIN:
            val = 0
            for cell in line:
                if(blocks[cell]==flag1):
                    val = val + 10
                elif(blocks[cell]==flag2):
                    val = val - 10
            if(val==20):
                val = val + 6
            if(val==-20):
                val = val - 6
            if(val==30):
                sum = sum + 10000
            elif(val==-30):
                sum = sum - 10000
            sum = sum + val
        if(blocks[4]==flag1):
            sum = sum + 5
        elif(blocks[4]==flag2):
            sum = sum - 5

        for i in [0,2,6,8]:
            if(blocks[i] == flag1):
                sum = sum + 4
            elif(blocks[i]==flag2):
                sum = sum -4
            
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
        """if sum(1 for row in board for i in row if i == '-') > 73:
            for choice in blocks_allowed:
                base = ((choice/3)*3+1, (choice%3)*3+1)
                if board[base[0]][base[1]] == '-':
                    pass#                    return base, 0
        """
        cells = self.get_empty_out_of(board, blocks_allowed, block)
        if(depth == 0):
            if(len(cells)>12):
                MAX_DEPTH = 3
            if(len(cells)>10):
                MAX_DEPTH = 4
            elif(len(cells)>7):
                MAX_DEPTH = 5
            else:
                MAX_DEPTH = 9
        # Process each in DFS
        move_dict = {}
        for move in cells:
            # Make temporary instance of the board
            temp_board = copy.deepcopy(board)
            temp_block = copy.deepcopy(block)
            # Apply the current move to the instance
            if depth%2 == 0:
                self.apply_move(temp_board, temp_block, move, flag)
            else:
                self.apply_move(temp_board, temp_block, move, self.flag_alternate[flag])                
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
        if(old_move==(-1,-1)):
            return (4,4)
        self.myflag = flag
        m, v = self.dfs_best_move(board, block, old_move, flag, 0, None, None)
	return m

