from collections import deque, defaultdict
from itertools import combinations, product, permutations
from queue import PriorityQueue
from copy import deepcopy
import sys
input=sys.stdin.readline
board=[]
v,e=map(int,input().split())
ans=1e9
for i in range(v+1):
    board.append([1e9]*(v+1))

for i in range(e):
    a,b,c=map(int,input().split())
    board[a][b]=c

for k in range(1,v+1):
    for i in range(1,v+1):
        for j in range(1,v+1):
            board[i][j]=min(board[i][j],board[i][k]+board[k][j])


for i in range(1,v+1):
    ans=min(ans,board[i][i])

if ans==1e9:
    print(-1)
else:
    print(ans)