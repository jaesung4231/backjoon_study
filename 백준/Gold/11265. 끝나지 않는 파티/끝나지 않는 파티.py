import sys
from itertools import combinations
N,M=map(int,input().split())
board=[]
graph=[[1e9]*N for _ in range(N)]
for i in range(N):
    board.append(list(map(int,input().split())))

for k in range(N):
    for i in range(N):
        for j in range(N):
            if board[i][j]>board[i][k]+board[k][j]:
                board[i][j]=board[i][k]+board[k][j]

for i in range(M):
    a,b,c=map(int,input().split())
    if board[a-1][b-1]<=c:
        print("Enjoy other party")
    else:
        print("Stay here")