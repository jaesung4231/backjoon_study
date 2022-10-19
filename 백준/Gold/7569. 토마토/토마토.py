from collections import deque
from copy import deepcopy
import sys
input=sys.stdin.readline
M,N,H=map(int,input().split())
tomato=[]
day=[]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

up=[N,-N]
down=[0,0]

def bfs(T):
    queue=deque()
    for i in range(len(T)):
     queue.append([T[i][0],T[i][1]])

    while(queue):
        a,b=queue.popleft()
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if -1<nx<(N*H) and -1<ny<M and nx//N==a//N:
                if tomato[nx][ny]==0:
                    tomato[nx][ny]=1
                    queue.append([nx,ny])
                    if day[nx][ny]==0:
                        day[nx][ny]=day[a][b]+1
        for i in range(2):
            nx=a+up[i]
            ny=b
            if -1<nx<(N*H) and -1<ny<M:
                if tomato[nx][ny]==0:
                    tomato[nx][ny]=1
                    queue.append([nx,ny])
                    if day[nx][ny]==0:
                        day[nx][ny]=day[a][b]+1



T=[]

for i in range(H*N):
    tomato.append(list(map(int,input().split())))
    day.append([0]*M)

for i in range(H*N):
    for j in range(M):
        if tomato[i][j]==1:
            T.append([i,j])
bfs(T)
MAX=-1
count=0
for i in range(H*N):
    for j in range(M):
        if tomato[i][j]==0:
            count+=1
            break
        elif day[i][j]>MAX:
                MAX=day[i][j]

if count!=0:
    print(-1)
else:
    print(MAX)

