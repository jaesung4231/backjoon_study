import sys
import math
from collections import deque
from itertools import combinations
input=sys.stdin.readline
N=int(input())
board=[[] for _ in range(N)]
tmp=0
answer=[1,2]

for i in range(N*5):
    board[i//5].append(list(input().strip()))

def check(a,b):
    cnt=0
    for i in range(5):
        for j in range(7):
            if board[a][i][j]==board[b][i][j]:
                cnt+=1
    return cnt

for c in combinations(range(N),2):
    cost=check(c[0],c[1])
    if tmp<cost:
       answer=[c[0]+1,c[1]+1] 
       tmp=cost

print(*answer)

