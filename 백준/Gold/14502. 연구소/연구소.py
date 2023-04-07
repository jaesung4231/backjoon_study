from collections import deque, defaultdict
from itertools import combinations, product, permutations
from copy import deepcopy
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
board=[]
blank=[]
dx=[-1,1,0,0]
dy=[0,0,1,-1]
for i in range(n):
    board.append(list(map(int,input().split())))

def pb(board):
    for i in range(n):
        print(board[i])
    print("==================")

def copy():
    tmp=[]
    for i in range(n):
        tmp.append(board[i][:])
    return tmp

def bfs(x,y,board):
    visited=defaultdict(int)
    queue=deque()
    queue.append([x,y])
    visited[x,y]
    while queue:
        a,b=queue.popleft()
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if -1<nx<n and -1<ny<m and board[nx][ny]==0 and (nx,ny) not in visited:
                board[nx][ny]=2
                queue.append([nx,ny])
                visited[nx,ny]


wall=0  

for i in range(n):
    for j in range(m):
        if board[i][j]==0:
            blank.append([i,j])
        if board[i][j]==1:
            wall+=1


tmp=copy()
answer=-1

for idx in combinations(blank,r=3):
    tmp=copy()
    num=0
    for i in idx:
        tmp[i[0]][i[1]]=1
    
    for i in range(n):
        for j in range(m):
            if tmp[i][j]==2:
                bfs(i,j,tmp)
    
    for i in range(n):
        for j in range(m):
            if tmp[i][j]==0:
                num+=1
    
    answer=max(answer,num)

print(answer)

    

