import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
board=[]
visited=[[0]*n for i in range(n)]

dx=[-1,1,0,0]
dy=[0,0,1,-1]

for i in range(n):
    board.append(list(input().strip()))

def normal(x,y):
    queue=deque()
    queue.append([x,y])
    visited[x][y]=1
    while queue:
        a,b=queue.popleft()
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if -1<nx<n and -1<ny<n and visited[nx][ny]==0 and board[nx][ny]==board[a][b]:
                queue.append([nx,ny])
                visited[nx][ny]=1
ans=0
for i in range(n):
    for j in range(n):
        if visited[i][j]==0:
            normal(i,j)
            ans+=1

ans2=0
for i in range(n):
    for j in range(n):
        visited[i][j]=0
        if board[i][j]=='R':
            board[i][j]='G'


for i in range(n):
    for j in range(n):
        if visited[i][j]==0:
            normal(i,j)
            ans2+=1
 
print(ans,ans2)

