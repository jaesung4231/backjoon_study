from collections import deque
import sys
input=sys.stdin.readline
N,M=map(int,(input().split()))
maze=[]
ans=[]
for i in range(N):
    ans.append([0]*M)
ans[0][0]=1

for i in range(N):
    maze.append(list(map(int,input().strip())))

dx=[1,-1,0,0]
dy=[0,0,-1,1]

def bfs(x,y,cnt):
    maze[x][y]=0
    result=deque()
    result.append([x,y])
    ans[x][y]=1
    while result:
        a,b=result.popleft()
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if -1<nx<N and -1<ny<M and maze[nx][ny]==1:
                maze[nx][ny]=0
                if ans[nx][ny]==0:
                  ans[nx][ny]=ans[a][b]+1
                result.append([nx,ny])
    return cnt

result=[]
result.append(bfs(0,0,0))
print(ans[N-1][M-1])
# print(result)
