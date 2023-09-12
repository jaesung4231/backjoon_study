import sys
from collections import deque, defaultdict
input=sys.stdin.readline
N=int(input())
board=[list(map(int,input().split())) for _ in range(N)]
visit=[[0]*N for _ in range(N)]
move=[[1,0],[0,1]]

def pb(board):
    for b in board:
        print(b)
    print("===============")

def bfs(x,y):
    queue=deque()
    queue.append([x,y])
    visit[x][y]=1
    while queue:
        a,b=queue.popleft()
        if a==N-1 and b==N-1:
            return
        for i in range(2):
            nx=a+(move[i][0]*board[a][b])
            ny=b+(move[i][1]*board[a][b])
            if -1<nx<N and -1<ny<N and visit[nx][ny]==0:
                visit[nx][ny]=1
                queue.append([nx,ny])
bfs(0,0)

if visit[N-1][N-1]==1:
    print("HaruHaru")
else:
    print("Hing")
