import sys
from collections import deque, defaultdict
input=sys.stdin.readline
n,m,a,b=map(int,input().split())
board=[]
item=[]
tmp=[]
bomb=defaultdict(int)

for _ in range(n):
    board.append([0]*m)
    tmp.append(['0']*m)

for i in range(a):
    x,y=map(int,input().split())
    item.append([x-1,y-1])
    tmp[x-1][y-1]="s"

board[0][0]=1

for i in range(b):
    x,y=map(int,input().split())
    tmp[x-1][y-1]="x"
    bomb[x-1,y-1]

def pb(board):
    for i in range(n):
        print(board[i])
    print("================")


def find(x,y,tx,ty):
    for i in range(x,tx+1):
        if (i,y) in bomb: 
            board[i][y]=0
            break
        else:
            board[i][y]=board[x][y]
    for i in range(y,ty+1):
        if (x,i) in bomb:
            board[x][i]=0
            break
        else:
            board[x][i]=board[x][y]

    for i in range(x+1,tx+1):
        for j in range(y+1,ty+1):
            if (i,j) in bomb: 
                board[i][j]=0
                continue
            board[i][j]=board[i-1][j]+board[i][j-1]

item.sort()
find(0,0,item[0][0],item[0][1])
for i in range(a-1):
    find(item[i][0],item[i][1],item[i+1][0],item[i+1][1])    
find(item[a-1][0],item[a-1][1],n-1,m-1)
print(board[n-1][m-1])

    