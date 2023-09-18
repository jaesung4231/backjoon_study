import sys
import math
from collections import deque
input=sys.stdin.readline
N=int(input())
M=int(input())
board=[]
move=[[1,0],[]]
for i in range(N):
    board.append([0]*N)

cnt=N**2
board[N//2][N//2]=1
ans=[]
for k in range(N//2):
    for i in range(k,N-k):
        board[i][k]=cnt
        cnt-=1

    for i in range(k+1,N-k-1):
        board[N-k-1][i]=cnt
        cnt-=1
    
    for i in range(k,N-k):
        board[N-i-1][N-k-1]=cnt
        cnt-=1

    for i in range(k+1,N-k-1):
        board[k][N-i-1]=cnt
        cnt-=1

for i in range(N):
    for j in range(N):
        print(board[i][j], end=" ")
        if board[i][j]==M: ans=[i+1,j+1]
    print()
print(*ans)
        
