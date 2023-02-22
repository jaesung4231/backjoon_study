from collections import deque, defaultdict
from copy import deepcopy
from itertools import permutations, combinations, product
import sys
input=sys.stdin.readline
t=int(input())
board=[]
ans=0

def pb(b):
    for i in range(t):
        print(b[i])
    print('===================')


def move(d,board):
    # 왼쪽으로 밀기
    if d==1:
      for i in range(t):
            start=(board[i][0],0)
            for j in range(t-1):
                if start[0]==board[i][j+1]:
                    board[i][start[1]]+=board[i][j+1]
                    board[i][j+1]=0
                    start=(board[i][j+1],j+1)
                elif board[i][j+1]!=0:
                    start=(board[i][j+1],j+1)
        
            for j in range(t):
                if board[i][j]==0:
                    for k in range(j,t):
                        if board[i][k]!=0:
                            board[i][j]=board[i][k]
                            board[i][k]=0
                            break
    # 오른쪽으로 밀기        
    elif d==2:
        for i in range(t):
            start=(board[i][t-1],t-1)
            for j in range(t-1,0,-1):
                if start[0]==board[i][j-1]:
                    board[i][start[1]]+=board[i][j-1]
                    board[i][j-1]=0
                    start=(board[i][j-1],j-1)
                elif board[i][j-1]!=0:
                    start=(board[i][j-1],j-1)

            for j in range(t-1,-1,-1):
                if board[i][j]==0:
                    for k in range(j,-1,-1):
                        if board[i][k]!=0:
                            board[i][j]=board[i][k]
                            board[i][k]=0
                            break            
    # 위로 밀기  
    elif d==3:
        for j in range(t):
            start=(board[0][j],0)
            for i in range(t-1):
                if start[0]==board[i+1][j]:
                    board[start[1]][j]+=board[i+1][j]
                    board[i+1][j]=0
                    start=(board[i+1][j],i+1)
                elif board[i+1][j]!=0:
                    start=(board[i+1][j],i+1)

            for i in range(t):
                if board[i][j]==0:
                    for k in range(i,t):
                        if board[k][j]!=0:
                            board[i][j]=board[k][j]
                            board[k][j]=0
                            break
    # 아래로 밀기
    elif d==4:
        for j in range(t):
            start=(board[t-1][j],t-1)
            for i in range(t-1,0,-1):
                if start[0]==board[i-1][j]:
                    board[start[1]][j]+=board[i-1][j]
                    board[i-1][j]=0
                    start=(board[i-1][j],i-1)
                elif board[i-1][j]!=0:
                    start=(board[i-1][j],i-1)

            for i in range(t-1,-1,-1):
                if board[i][j]==0:
                    for k in range(i,-1,-1):
                        if board[k][j]!=0:
                            board[i][j]=board[k][j]
                            board[k][j]=0
                            break   

    
for i in range(t):
    board.append(list(map(int,input().split())))

ans=0

p=[]
for i in product([1,2,3,4],repeat=5):
    tmp=[]
    for u in range(t):
        tmp.append(board[u][:])
    for j in i:
        move(j,tmp)
    for k in range(t):
        for l in range(t):
            ans=max(ans,tmp[k][l])
        

print(ans)

