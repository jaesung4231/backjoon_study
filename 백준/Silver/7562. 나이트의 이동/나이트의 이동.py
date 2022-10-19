from collections import deque
from copy import deepcopy
import sys
input=sys.stdin.readline
N=int(input())
cb=[]


dx=[-2,-2,-1,-1,2,2,1,1]
dy=[1,-1,2,-2,-1,1,-2,2]

def bfs(x,y,board):
    queue=deque()
    queue.append([x,y])
    while(queue):
        a,b=queue.popleft()
        for i in range(8):
            nx=a+dx[i]
            ny=b+dy[i]
            if -1<nx<T and -1<ny<T and board[nx][ny]==0:
                board[nx][ny]=board[a][b]+1
                queue.append([nx,ny])

        
for i in range(N):
    T=int(input())
    cb=[]
    for j in range(T):
        cb.append([0]*T)
    x,y=map(int, input().split())
    cb[x][y]=1
    bfs(x,y,cb)
    dtx,dty=map(int,input().split())
    print(cb[dtx][dty]-1)


