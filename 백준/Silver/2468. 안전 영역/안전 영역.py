import sys
import copy
from copy import deepcopy
from collections import deque
N= int(sys.stdin.readline())
ans=[]
Area=[]
for i in range(N):
    Area.append(list(map(int,sys.stdin.readline().split())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(i,j,k,tmp):
    tmp[i][j]=0
    queue= deque()
    queue.append([i,j])
    while(queue):
        a,b=queue.popleft()
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if -1<nx<N and -1<ny<N and tmp[nx][ny]>k:
                tmp[nx][ny]=0
                queue.append([nx,ny])

for k in range(0,101):
    cnt=0
    tmp=deepcopy(Area)
    for i in range(N):
        for j in range(N):
            if(tmp[i][j]>k):
                bfs(i,j,k,tmp)
                cnt+=1
    ans.append(cnt)

print(max(ans))