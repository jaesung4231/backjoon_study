from collections import deque, defaultdict
from itertools import combinations, product, permutations
from copy import deepcopy
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
board=[]
visited={}
dx=[-1,1,0,0]
dy=[0,0,-1,1]
answer=0
MAX=-1


def dfs(L,x,y,visited,total):
    global answer
    if answer>=total+((4-L)*MAX):
        return
    if L==4:
        answer=max(answer,total)
        return
    else:
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if -1<nx<n and -1<ny<m and (nx,ny) not in visited:
                if L==2:
                    visited[nx,ny]=1
                    dfs(L+1,x,y,visited,total+board[nx][ny])
                    del visited[nx,ny]
                visited[nx,ny]=1
                dfs(L+1,nx,ny,visited,total+board[nx][ny])
                del visited[nx,ny]

            
for i in range(n):
    data=list(map(int,input().split()))
    MAX=max(MAX,max(data))
    board.append(data)


for i in range(n):
    for j in range(m):
        visited[i,j]=1
        dfs(1,i,j,visited,board[i][j])    
        del visited[i,j]

print(answer)


