from collections import deque, defaultdict
from copy import deepcopy
from itertools import permutations, combinations, product
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
board=[]
cplace=[]
num=0   
answer=int(1e9)
mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]],
]

dx=[-1,0,1,0]
dy=[0,1,0,-1]

for i in range(n):
    board.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        if board[i][j]!=0 and board[i][j]!=6:
            cplace.append([i,j,board[i][j]])
            num+=1

def move(board,mm,x,y):
    for i in mm:
        nx=x
        ny=y
        while True:
            nx+=dx[i]
            ny+=dy[i]
            if  nx<0 or ny<0 or nx>=n or ny>=m:
                break
            if board[nx][ny]==6:
                break
            if board[nx][ny]==0:
                board[nx][ny]='#'



def dfs(L,board):
    global answer
    if L==num:
        cnt=0
        for i in range(n):
            for j in range(m):
                if board[i][j]==0:
                    cnt+=1
        answer=min(cnt,answer)
        return
    else:
        x,y,ty=cplace[L]
        tmp=deepcopy(board)
        for i in mode[ty]:
            move(tmp,i,x,y)
            dfs(L+1,tmp)
            tmp=deepcopy(board)

dfs(0,board)
print(answer)