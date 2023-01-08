from collections import deque
import sys
input=sys.stdin.readline

n,m,k=map(int,input().split())
board=[]
visited=[[[0]*(k+1) for _ in range(m)] for _ in range(n)]

dx=[1,-1,0,0]
dy=[0,0,1,-1]

for i in range(n):
     board.append(list(input().strip()))


def bfs(k):
    visited[0][0][k]=1
    queue=deque()
    queue.append([0,0,k])
    while(queue):
        a,b,c=queue.popleft()
        if a==n-1 and b==m-1:
            print(visited[a][b][c])
            return
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if -1<nx<n and -1<ny<m:
                if c>0 and board[nx][ny]=='1' and visited[nx][ny][c-1]==0:
                    queue.append([nx,ny,c-1])
                    visited[nx][ny][c-1]=visited[a][b][c]+1
                if board[nx][ny]=='0' and visited[nx][ny][c]==0:
                    queue.append([nx,ny,c])
                    visited[nx][ny][c]=visited[a][b][c]+1
    print(-1)

bfs(k)
# print_visited()








