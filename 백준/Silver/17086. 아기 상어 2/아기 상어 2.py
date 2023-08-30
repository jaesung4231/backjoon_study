import sys
from collections import deque, defaultdict
input=sys.stdin.readline
N,M=map(int,input().split())
move=[[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
board=[]
check=[]
ans=0

for i in range(N):
    board.append(list(map(int,input().split())))

def bfs(x,y):
    global ans
    queue=deque()
    queue.append([x,y])
    visited=defaultdict(int)
    visited[(x,y)]=0
    while queue:
        a,b=queue.popleft()
        for i in range(8):
            nx=a+move[i][0]
            ny=b+move[i][1]
            if -1<nx<N and -1<ny<M and (nx,ny) not in visited:
                if board[nx][ny]==1:
                    ans=max(ans,visited[(a,b)]+1)
                    return visited[(a,b)]
                visited[(nx,ny)]=visited[(a,b)]+1
                queue.append([nx,ny])

for i in range(N):
    for j in range(M):
        if board[i][j]!=1:
            bfs(i,j)
            

print(ans)