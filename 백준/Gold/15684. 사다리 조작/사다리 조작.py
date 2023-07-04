from collections import deque, defaultdict
from itertools import combinations, product, permutations
from copy import deepcopy
import heapq
import sys
input=sys.stdin.readline
n,m,h=map(int,input().split())
board=[]
move=[[0,0],[0,-1]]
move_c=[[0,1],[0,-1]]
ans=1e9

for i in range(h):
    board.append([0]*n)


for i in range(m):
    a,b=map(int,input().split())
    board[a-1][b-1]=1



def pb(board):
    for i in range(h):
        print(board[i])
    print("=============")


def check():
    for i in range(n):
        k=i
        for j in range(h):
            if board[j][k]==1:
                k+=1
            elif k>0 and board[j][k-1]:
                k-=1
        if k!=i: return False
    return True


def dfs(L,x,y):
    global ans
    made=True
    # pb(board)
    if L>3 or L>=ans:
        return
    
    if check():
        ans=min(L,ans)
        return
    
    for i in range(x,h):
        for j in range(n-1):
            if board[i][j]==1:
                continue
            elif board[i][j]==0 and board[i][j+1]==0:
                board[i][j]=1
                dfs(L+1,i,j)
                board[i][j]=0


dfs(0,0,0)

if ans==1e9:
    print(-1)
else:
    print(ans)

