from collections import deque, defaultdict
from copy import deepcopy
from itertools import permutations, combinations, product
import sys
input=sys.stdin.readline
a,b,c=map(int,input().split())
board=[]
answer=0
for i in range(a):
    board.append([0]*b)
stikers=[]

def turn(x):
    row=len(x)
    col=len(x[0])
    tmp=[[0]*row for _ in range(col)]
    for i in range(col):
        for j in range(row):
            tmp[i][j]=x[row-j-1][i]
    return tmp

def search(x,y,n,m,stik):
    if x+n>a or y+m>b:
        return False
    for i in range(n):
        for j in range(m):
            if board[x+i][y+j]==1 and stik[i][j]==1:
                return False
    return True

def fill(x,y,n,m,stik):
    global answer
    for i in range(n):
        for j in range(m):
            if board[x+i][y+j]==0 and stik[i][j]==1:
                board[x+i][y+j]=stik[i][j]
                answer+=1


def check(stiker):
    isTrue=False
    for i in range(a):
        for j in range(b):
            if search(i,j,len(stiker),len(stiker[0]),stiker):
                fill(i,j,len(stiker),len(stiker[0]),stiker)
                return True
    return False
            # else:
            #     for _ in range(4):
            #         stiker=turn(stiker)
            #         if search(i,j,len(stiker),len(stiker[0]),stiker):
            #             fill(i,j,len(stiker),len(stiker[0]),stiker)
            #             return


for i in range(c):
    tmp=[]
    n,m=map(int,input().split())
    for i in range(n):
        tmp.append(list(map(int,input().split())))
    stikers.append(tmp)

for stiker in stikers:
    if check(stiker)==False:
        for _ in range(4):
            stiker=turn(stiker)
            if check(stiker)==True:
                break

# for i in range(a):
#     print(board[i])

print(answer)
    

