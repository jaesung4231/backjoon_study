from itertools import permutations
from collections import deque
import sys
input=sys.stdin.readline
n,l,r=map(int,input().split())
board=[]
dx=[-1,1,0,0]
dy=[0,0,1,-1]

for i in range(n):
    board.append(list(map(int,input().split())))


def pb(board):
    for i in range(len(board)):
        print(board[i])


def bfs(x,y,visited):
    queue=deque()
    queue.append([x,y])
    visited[x][y]=1
    open=[[x,y]]
    total=board[x][y]
    size=1
    
    while queue:
        a,b =queue.popleft()
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if -1<nx<n and -1<ny<n and visited[nx][ny]==0:
                p=abs(board[a][b]-board[nx][ny])
                if p>=l and p<=r:
                    queue.append([nx,ny])
                    open.append([nx,ny])
                    total+=board[nx][ny]
                    visited[nx][ny]=1
                    size+=1
   
    for idx in open:
        board[idx[0]][idx[1]]=total//size
    
    if len(open)>1:
        return True
    else:
        return False
ans=0
while(1):
    opened=False
    visited=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j]==0:
                if bfs(i,j,visited):
                    opened=True
                    
    if opened==False:
        break
    else:
        ans+=1
    

# pb(board)
print(ans)



