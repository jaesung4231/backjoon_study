from collections import deque
from copy import deepcopy
import sys
input=sys.stdin.readline
board=[]
ans=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

N=int(input())

for i in range(N):
    board.append(list(input().strip()))

def bfs(x,y):
    cnt=1
    board[x][y]='S'
    queue=deque()
    queue.append([x,y])
    while(queue):
        a,b=queue.popleft()
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if -1<nx<N and -1<ny<N and board[nx][ny]=='1':
                queue.append([nx,ny])
                board[nx][ny]='S'
                cnt+=1
    return cnt


for i in range(N):
    for j in range(N):
        if(board[i][j]=='1'):
            ans.append((bfs(i,j)))

ans.sort()
print(len(ans))
for i in range(len(ans)):
    print(ans[i])


