import sys
import math
from collections import deque
from itertools import combinations
input=sys.stdin.readline
board=[]
N,M=map(int,input().split())
cnt=0
for _ in range(N):
    board.append(list(map(int,input().strip())))

def pb():
    for b in board:
        print(b)
    print("==============")


def flip(x,y):
    for i in range(x+1):
        for j in range(y+1):
            if board[i][j]==1:
                board[i][j]=0
            else:
                board[i][j]=1


def bfs(x,y):
    global cnt
    queue=deque()
    queue.append([x,y])
    while queue:
        a,b=queue.popleft()
        if board[a][b]==1:
            flip(a,b)
            cnt+=1
        nx=a-1
        ny=b+1
        if -1<nx<N and -1<ny<M:
            queue.append([nx,ny])

for i in range(M-1,-1,-1):
    bfs(N-1,i)

for i in range(N-2,-1,-1):
    bfs(i,0)

print(cnt)


