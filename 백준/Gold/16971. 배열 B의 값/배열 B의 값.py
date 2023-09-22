import sys
import math
from collections import deque
from itertools import combinations
input=sys.stdin.readline
N,M=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(N)]
def make(board):
    tmp=0
    for i in range(N-1):
        for j in range(M-1):
            tmp+=(board[i][j]+board[i+1][j]+board[i+1][j+1]+board[i][j+1])    
    return tmp

def exchange_row(a,b):
    boardtmp=[]
    for bo in board:
        boardtmp.append(bo[:])
    tmp=boardtmp[a][:]
    boardtmp[a]=board[b][:]
    boardtmp[b]=tmp[:]
    return make(boardtmp)
 
    
def exchange_col(a,b):
    boardtmp=[]
    for bo in board:
        boardtmp.append(bo[:])
    tmp=[]
    for i in range(N):
        tmp.append(boardtmp[i][a])
        boardtmp[i][a]=board[i][b]
    for i in range(N):
        boardtmp[i][b]=tmp[i]
    
    return make(boardtmp)

row=[0]*N
col=[0]*M

row_min=1e9
col_min=1e9

row_idx=-1
col_idx=-1

for i in range(N):
    for j in range(M):
        row[i]+=board[i][j]
        col[j]+=board[i][j]

for i in range(1,N-1):
    tmp=row[i]*4
    tmp-=2*(board[i][0]+board[i][M-1])
    if row_min>tmp:
        row_idx=i
        row_min=tmp

for i in range(1,M-1):
    tmp=col[i]*4
    tmp-=2*(board[0][i]+board[N-1][i])
    if col_min>tmp:
        col_idx=i
        col_min=tmp


ans=make(board)

if col_idx>0:
    ans=max(exchange_col(0,M-1),exchange_col(0,col_idx),exchange_col(M-1,col_idx),ans)
if row_idx>0:
    ans=max(exchange_row(0,N-1),exchange_row(0,row_idx),exchange_row(N-1,row_idx),ans)
print(ans)