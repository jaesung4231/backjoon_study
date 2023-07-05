from collections import deque, defaultdict
from itertools import combinations, product, permutations
from copy import deepcopy
import heapq
import sys
input=sys.stdin.readline
n=int(input())
node=defaultdict(int)
move=[[1,0],[0,-1],[-1,0],[0,1]]
box=[[1,0],[0,1],[1,1]]
board=[]
ans=0
for i in range(100):
    board.append([0]*100)

def pb(board):
    for i in range(len(board)):
        print(board[i])
    print("===========")

def turn(dir):
    if dir==3:
        return 0
    else:
        return dir+1

def draw(dir,k):
    curve=[dir]
    for i in range(k):
        for j in range(len(curve)-1,-1,-1):
            curve.append(turn(curve[j]))
    return curve

for i in range(n):
    x,y,d,g=map(int,input().split())
    spot=draw(d,g)
    nx=x
    ny=y
    node[nx,ny]+=1
    for s in spot:
        nx=nx+move[s][0]
        ny=ny+move[s][1]
        node[nx,ny]+=1
    # print(node)

for no in node:
    canbox=True
    for i in range(3):
        if (no[0]+box[i][0],no[1]+box[i][1]) not in node:
            canbox=False
            break
    if canbox:
        ans+=1
print(ans)