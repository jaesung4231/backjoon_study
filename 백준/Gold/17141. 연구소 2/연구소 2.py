from collections import deque, defaultdict
from itertools import combinations, product, permutations
from copy import deepcopy
import sys
input=sys.stdin.readline
board=[]
n,m=map(int,input().split())
virus=[]
dx=[-1,1,0,0]
dy=[0,0,1,-1]


def copy(board):
    tmp=[]
    for i in range(n):
        tmp.append(board[i][:])
    return tmp


def bfs(c,board,ans):
    queue=deque()
    for start in c:
        queue.append([start[0],start[1]])
        board[start[0]][start[1]]=1

    while queue:
        a,b=queue.popleft()
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if -1<nx<n and -1<ny<n and board[nx][ny]==0:
                queue.append([nx,ny])
                board[nx][ny]=board[a][b]+1
    return board[a][b]


ans=1e9
for i in range(n):
    board.append(list(map(int,input().split())))


for i in range(n):
    for j in range(n):
        if board[i][j]==2:
            virus.append([i,j])
            board[i][j]=0
        if board[i][j]==1:
            board[i][j]="-"


for c in combinations(virus,r=m):
    tmp=copy(board)
    num=bfs(c,tmp,ans)
    didfill=True
    for i in range(n):
        for j in range(n):
            if tmp[i][j]==0:
                didfill=False
                break
    if didfill==True:
        ans=min(num,ans)
if ans==1e9:
    print(-1)
else:
    print(ans-1)



