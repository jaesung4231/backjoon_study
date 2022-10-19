from collections import deque
from copy import deepcopy
import queue
import sys
input=sys.stdin.readline
N=int(input())
color=[]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y,color):
    ncol=color[x][y]
    color[x][y]=0
    queue=deque()
    queue.append([x,y])
    while(queue):
        a,b=queue.popleft()
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if -1<nx<N and -1<ny<N and color[nx][ny]==ncol:
                color[nx][ny]=0
                queue.append([nx,ny])

for i in range(N):
    color.append(list(input().strip()))

color_2=deepcopy(color)
for i in range(N):
    for j in range(N):
        if color_2[i][j]=='R' or color_2[i][j]=="G":
            color_2[i][j]='T'
            
cnt=0
cnt_2=0
for i in range(N):
    for j in range(N):
        if color[i][j]!=0:
            bfs(i,j,color)
            cnt+=1
        if color_2[i][j]!=0:
            bfs(i,j,color_2)
            cnt_2+=1

print(cnt, cnt_2)
# for i in range(N):
#     print(*color[i])

