import sys
from collections import deque
input = sys.stdin.readline


k=int(input())
n,m=map(int,input().split())
board=[]
visited =[[[0]* 3 for _ in range(m)]for _ in range(n)]

for i in range(m):
    board.append(list(input().split()))


hx=[2,2,-2,-2,1,-1,1,-1]
hy=[1,-1,1,-1,-2,-2,2,2]


dx=[-1,1,0,0]
dy=[0,0,-1,1]


def bfs(k):
    queue=deque()
    queue.append([0,0,k])
    visited =[[[0 for _ in range(k+1)] for _ in range(n)]for _ in range(m)]
    while queue:
        a,b,c=queue.popleft()
        if a==m-1 and b==n-1:
            print(visited[a][b][c])
            return
        if c>0:
            for i in range(8):
                nx=a+hx[i]
                ny=b+hy[i]
                if -1<nx<m and -1<ny<n and board[nx][ny]=='0' and visited[nx][ny][c-1]==0:
                    queue.append([nx,ny,c-1])
                    visited[nx][ny][c-1]=visited[a][b][c]+1
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if -1<nx<m and -1<ny<n and board[nx][ny]=='0' and visited[nx][ny][c]==0:
                queue.append([nx,ny,c])
                visited[nx][ny][c]=visited[a][b][c]+1
    
        # for i in range(m):
        #     print(visited)
        # print("=====================")
    print(-1)
bfs(k)




    




