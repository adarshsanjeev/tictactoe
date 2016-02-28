import sys
import random

WIN = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

mapping = {'x':1,'-':0,'o':-1}

def evaluate_block(self,block_id,board):
    power = 0 
    base = ((block_id//3)*3, (block_id%3)*3)
    block_id = base[0] + base[1]/3
    val = 0
    #ROWS
    for i in range(3):
        val = 0
        for j in range(3):
            val = val + mapping[board[base[0]+i][base[1]+j]]
        if val > 0 :
            power = power + pow(10,val)
        elif val < 0 :
            power = power - pow(10,val)
    
    #COLS
    for j in range(3):
        val = 0
        for i in range(3):
            val = val + mapping[board[base[0]+i][base[1]+j]]
        if val > 0 :
            power = power + pow(10,val)
        elif val < 0 :
            power = power - pow(10,val)
        
    val=0
    for i in range(3):
        val = val + mapping[board[base[0]+i][base[1]+i]]
    if val > 0 :
        power = power + pow(10,val)
    elif val < 0 :
        power = power - pow(10,val)
    
    val = 0
    for i in range(3):
        val = val + mapping[board[base[0]+i][base[1]+2-i]]
    if val > 0 :
        power = power + pow(10,val)
    elif val < 0 :
        power = power - pow(10,val)
    
    

def evaluate_board(self,board,blocks,flag1,flag2):
    sum = 0 
    for line in WIN:
        val = 0
        for cell in line:
            if(block[cell]==flag1):
                val+=1
            elif(block[cell]==flag2):
                val-=1
        if(val>0):
            sum = sum + 10*pow(10,val)
        elif(val<0):
            sum = sum - 10*pow(10,val)

    return sum 

