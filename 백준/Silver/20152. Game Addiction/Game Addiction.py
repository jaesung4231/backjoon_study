import sys
from collections import deque
input=sys.stdin.readline
H,N=map(int,input().split())
board=[[0]*31 for _ in range(31)]
sz=min(H,N)
ez=max(H,N)
for i in range(sz,31):
    board[sz][i]=1

for i in range(sz+1,31):
    for j in range(sz+1,31):
        if i>j: continue
        board[i][j]=board[i][j-1]+board[i-1][j]

print(board[ez][ez])