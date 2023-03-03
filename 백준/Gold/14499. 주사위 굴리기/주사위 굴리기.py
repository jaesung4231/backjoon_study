from collections import deque, defaultdict
from copy import deepcopy
from itertools import permutations, combinations, product
import sys
input=sys.stdin.readline
n,m,x,y,t=map(int,input().split())
dice=[0,0,0,0,0,0]
board=[]

#   2
# 4 1 3
#   5
#   6
# 
#   6
# 4 1 3
#   2
#   5
# 
#   5
# 4 6 3
#   1
#   2
# 
# 

def pb():
    for i in range(n):
        print(board[i])

def move_dice(num):
    if num==1:
        tmp=dice.pop(3)
        tmp2=dice.pop()
        dice.insert(1,tmp2)
        dice.append(tmp)
    elif num==2:
        tmp=dice.pop(1)
        tmp2=dice.pop()
        dice.insert(3,tmp2)
        dice.append(tmp)
    elif num==3:
        tmp=dice.pop(1)
        tmp2=dice.pop(2)
        tmp3=dice.pop(0)
        dice.append(tmp3)
        dice.insert(1,tmp)
        dice.insert(3,tmp2)
    elif num==4:
        tmp=dice.pop(1)
        tmp2=dice.pop(2)
        tmp3=dice.pop()
        dice.insert(0,tmp3)
        dice.insert(1,tmp)
        dice.insert(3,tmp2)
    
    # print(dice)


def check(x,y,dice):
    # print(board[x][y],n,m)
    if board[x][y]==0:
        board[x][y]=dice[5]
    else:
        dice[5]=board[x][y]
        board[x][y]=0
    print_ans()

# def check_bom(x,y,num):
#     if -1<x<n and -1<y<m:
#         print(board[x][y])
#         move_dice(num)

def print_ans():
    print(dice[2])



def move(num):
    global x
    global y
    if num==1:
        nx= x
        ny= y+1
        if -1<nx<n and -1<ny<m:
            x=nx
            y=ny
            move_dice(1)
            check(x,y,dice)
    elif num==2:
        nx=x
        ny=y-1
        if -1<nx<n and -1<ny<m:
            x=nx
            y=ny
            move_dice(2)
            check(x,y,dice)

    elif num==3:
        nx=x-1
        ny=y
        if -1<nx<n and -1<ny<m:
            x=nx
            y=ny
            move_dice(3)
            check(x,y,dice)
        
    elif num==4:
        nx=x+1
        ny=y
        if -1<nx<n and -1<ny<m:
            x=nx
            y=ny
            move_dice(4)
            check(x,y,dice)

for i in range(n):
    board.append(list(map(int,input().split())))

moves=list(map(int,input().split()))

for p in moves:
    move(p)






