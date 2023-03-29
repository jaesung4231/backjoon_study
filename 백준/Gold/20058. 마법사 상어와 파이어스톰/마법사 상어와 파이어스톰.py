from collections import deque, defaultdict
from itertools import combinations, product, permutations
from copy import deepcopy
import sys
input=sys.stdin.readline
n,q=map(int,input().split())
board=[]
next=[]
dx=[-1,1,0,0]
dy=[0,0,1,-1]
N=2**n
answer=0
for i in range(N):
    board.append(list(map(int,input().split())))
    next.append([0]*(N))
level=list(map(int,input().split()))


def pb(board):
    for i in range(N):
        print(board[i])


def pbox(box,L):
    for i in range(2**L):
        print(box[i])


def makeBox(L):
    tmp=[]
    for i in range(2**L):
        tmp.append([0]*(2**L))
    return tmp


def turn(box,L):
    tmp=[]
    for i in range(len(box)):
        p=[]
        for j in range(len(box)-1,-1,-1):
            p.append(box[j][i])
        tmp.append(p)
    return tmp


def choose(L,board):
    for i in range(N):
        for j in range(N):
            if i%(2**L)==0 and j%(2**L)==0:
                box=makeBox(L)
                for x in range(2**L):
                    for y in range(2**L):
                        box[x][y]=board[i+x][j+y]
                turnb=turn(box,L)
                for x in range(2**L):
                    for y in range(2**L):
                        next[i+x][j+y]=turnb[x][y]
    
    return next


def check(x,y,board,melt):
    ice=0
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if -1<nx<N and -1<ny<N and board[nx][ny]>0:
            ice+=1
    if ice<3:
        melt.append([x,y])

def bfs(x,y,visited):
    queue=deque()
    queue.append([x,y])
    visited[x,y]
    size=1
    while(queue):
        a,b=queue.popleft()
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if -1<nx<N and -1<ny<N and board[nx][ny]!=0 and (nx,ny) not in visited:
                visited[nx,ny]
                queue.append([nx,ny])
                size+=1
    return size



for l in level:
    next=choose(l,board)
    melt=[]
    for i in range(N):
        for j in range(N):
            if next[i][j]!=0:
                check(i,j,next,melt)
    for m in melt:
        next[m[0]][m[1]]-=1
                
    for i in range(N):
        board[i]=next[i][:]


visited=defaultdict(int) 
chunk=0
for i in range(N):
    for j in range(N):
        if board[i][j]!=0:
            answer+=board[i][j]
            if (i,j) not in visited:
                chunk=max(bfs(i,j,visited),chunk)


print(answer)
print(chunk)

            



