import sys
import heapq
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())

board=[]
visit=[]
dx=[-1,1,0,0,1,-1,-1,1]
dy=[0,0,1,-1,1,-1,1,-1]
cnt=0

for i in range(n):
    board.append(list(map(int,input().split())))
    visit.append([0]*m)

def bfs(x,y):
    queue=deque()
    queue.append([x,y])
    while queue:
        a,b=queue.popleft()
        for i in range(8):
            nx=a+dx[i]
            ny=b+dy[i]
            if -1<nx<n and -1<ny<m and board[nx][ny]==1 and visit[nx][ny]==0:
                visit[nx][ny]=1
                queue.append([nx,ny])

for i in range(n):
    for j in range(m):
        if visit[i][j]==0 and board[i][j]==1:
            bfs(i,j)
            cnt+=1

print(cnt)
