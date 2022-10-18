from collections import deque
import queue
import sys
input=sys.stdin.readline
T=int(input())
farm=[]


dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    farm[x][y]=0
    queue=deque()
    queue.append([x,y])
    while(queue):
        a,b=queue.popleft()
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if -1<nx<N and -1<ny<M and farm[nx][ny]==1:
                farm[nx][ny]=0
                queue.append([nx,ny])



for i in range(T):
    N,M,B=map(int,input().split())
    farm=[]
    place=[]
    cnt=0
    for i in range(N):
        farm.append([0]*M)
    for i in range(B):
        x,y=map(int,input().split())
        farm[x][y]=1
    for i in range(N):
        for j in range(M):
            if farm[i][j]==1:
                bfs(i,j)
                cnt+=1
    print(cnt)





