from collections import deque, defaultdict
from itertools import combinations, product, permutations
from copy import deepcopy
import sys
input=sys.stdin.readline
n=int(input())
board=[]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(n):
    board.append(list(map(int,input().split())))

def pb(board):
    for i in range(n):
        print(board[i])
    print("==================")

def make():
    tmp=[]
    for i in range(n):
        tmp.append([0]*n)
    return tmp

def bfs(L,x,y):
    global cnt
    global size
    global grow
    queue=deque()
    queue.append([x,y])
    tt=make()
    visited=defaultdict(int)
    visited[x,y]
    eat=[]
    tt[x][y]=0
    while(queue):
        a,b=queue.popleft()
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if -1<nx<n and -1<ny<n and (nx,ny) not in visited and board[nx][ny]<=size:
                if board[nx][ny]!=0 and board[nx][ny]<size:
                    eat.append([nx,ny,tt[a][b]+1])
                    queue.append([nx,ny])
                    visited[nx,ny]
                    tt[nx][ny]=tt[a][b]+1
                if board[nx][ny]==0 or board[nx][ny]==size:
                    queue.append([nx,ny])
                    visited[nx,ny]
                    tt[nx][ny]=tt[a][b]+1
  
    if len(eat)!=0:
        # print(eat,size,grow)
        # pb(board)
        eat.sort(key=lambda x: (x[2],x[0],x[1]))
        grow+=1
        if grow==size:
            size+=1
            grow=0
        board[eat[0][0]][eat[0][1]]=0
        cnt-=1
        bfs(L+eat[0][2],eat[0][0],eat[0][1])
    else:
        print(L)

cnt=0
s=[0,0]
size=2
grow=0
for i in range(n):
    for j in range(n):
        if board[i][j]==9:
            board[i][j]=0
            s[0]=i
            s[1]=j
        elif board[i][j]!=0:
            cnt+=1

bfs(0,s[0],s[1])
