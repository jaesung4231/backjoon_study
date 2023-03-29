from collections import deque, defaultdict
from itertools import combinations, product, permutations
from copy import deepcopy
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
move=[[0,0],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1]]
dx=[-1,-1,1,1]
dy=[1,-1,-1,1]

board=[]
command=[]
clouds=[[n-1,0],[n-1,1],[n-2,0],[n-2,1]]

for i in range(n):
    board.append(list(map(int,input().split())))


for i in range(m):
    d,s=map(int,input().split())
    command.append([d,s])

def pb(board):
    for i in range(n):
        print(board[i])
    print("=============")

def copy(x,y):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if -1<nx<n and -1<ny<n and board[nx][ny]!=0:
            board[x][y]+=1

def move_clouds(co,clouds):
    new=[]
    visited=[]
    for i in range(n):
        visited.append([0]*n)


    for cloud in clouds:
        nx=cloud[0]
        ny=cloud[1]
        for _ in range(co[1]):
            nx=nx+move[co[0]][0]
            ny=ny+move[co[0]][1]
            if nx<0:
                nx=n-1
            elif nx>n-1:
                nx=0  
            if ny<0:
                ny=n-1
            elif ny>n-1:
                ny=0
        new.append([nx,ny])
    
    for i in new:
        visited[i[0]][i[1]]=1
        board[i[0]][i[1]]+=1
    for i in new:
        copy(i[0],i[1])
    
    tmp=[]
    for i in range(n):
        for j in range(n):
            if visited[i][j]==0 and board[i][j]>=2:
                board[i][j]-=2
                tmp.append([i,j])

    return tmp

for co in command:
    clouds=move_clouds(co,clouds)

ans=0

for i in range(n):
    for j in range(n):
        ans+=board[i][j]

print(ans)
    
                
