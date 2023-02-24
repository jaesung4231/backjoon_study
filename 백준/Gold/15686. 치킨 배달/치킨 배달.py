from collections import deque, defaultdict
from copy import deepcopy
from itertools import permutations, combinations, product
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
board=[]
chicken=[]
house=[]
distance=[]

def pb(board):
    for i in range(n):
        print(board[i])


for i in range(n):
    board.append(list(map(int,input().split())))


for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            house.append([i,j])
        if board[i][j]==2:
            chicken.append([i,j])

ans=1e9
for d in combinations(chicken,m):
    distance=[]
    for i in range(len(house)):
        dis=1e9
        for j in d:
            dis=min(dis,(abs(house[i][0]-j[0])+abs(house[i][1]-j[1])))
        distance.append(dis)
    ans=min(ans, sum(distance))
print(ans)
    

