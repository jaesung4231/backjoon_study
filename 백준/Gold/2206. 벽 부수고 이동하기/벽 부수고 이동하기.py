import sys
from collections import deque
input=sys.stdin.readline

n, m = map(int, input().split())
board=[]
visted =[[[0]* 2 for _ in range(m)]for _ in range(n)]

for i in range(n):
    board.append(list(input().strip()))

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def print_board():
    for i in range(n):
        print(visted[i])

def bfs(i,j):
    queue=deque()
    queue.append([i,j,0])
    while(queue):
        a,b,c=queue.popleft()
        if a== n-1 and b==m-1:
            print(visted[a][b][c]+1)
            return
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if -1<nx<n and -1<ny<m :
                if board[nx][ny]=='0' and visted[nx][ny][c]==0 :
                    queue.append([nx,ny,c])
                    visted[nx][ny][c]=visted[a][b][c]+1
                if board[nx][ny]=='1' and c==0:
                    queue.append([nx,ny,1])
                    visted[nx][ny][1]=visted[a][b][0]+1
    print(-1)

bfs(0,0)