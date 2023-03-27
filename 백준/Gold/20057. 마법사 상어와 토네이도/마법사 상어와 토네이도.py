from collections import deque, defaultdict
from itertools import combinations, product, permutations
from copy import deepcopy
import sys
input=sys.stdin.readline
N=int(input())
board=[]
move=[[0,-1],[1,0],[0,1],[-1,0]]
dx=[1,-1]
t_map=[]
tornado=[]
out=0

tmp=0
for i in range(N):
    data=list(map(int,input().split()))
    tmp+=sum(data)
    board.append(data)


def getsum():
    t=0
    for i in range(N):
        t+=sum(board[i])
    return t

def pb(board):
    for i in range(N):
        print(board[i])
    print("==================")

# x,y 태풍이 시작하는는
def sand(dir,x,y):
    global out
    yx=x+move[dir][0]
    yy=y+move[dir][1]
    y_sand=board[yx][yy]
    total=y_sand
    if dir==0 or dir==2:
        for i in range(2):
            nx=yx+dx[i]
            ny=yy
            ss=int(y_sand*(7/100))
            total-=ss
            if -1<nx<N and -1<ny<N:
                board[nx][ny]+=ss
            else:
                out+=ss
        for i in range(2):
            nx=yx+dx[i]
            ny=yy+move[dir][1]
            ss=int(y_sand*(10/100))
            total-=ss
            if -1<nx<N and -1<ny<N:
                board[nx][ny]+=ss
            else:
                out+=ss
        for i in range(2):
            nx=yx+(dx[i]*2)
            ny=yy
            ss=int(y_sand*(2/100))
            total-=ss
            if -1<nx<N and -1<ny<N:
                board[nx][ny]+=ss
            else:
                out+=ss
        for i in range(2):
            nx=x+dx[i]
            ny=y
            ss=int(y_sand*(1/100))
            total-=ss
            if -1<nx<N and -1<ny<N:
                board[nx][ny]+=ss
            else:
                out+=ss
        ss=int(y_sand*(5/100))
        if -1<yy+(move[dir][1])*2<N and -1<yy<N:
            board[yx][yy+(move[dir][1])*2]+=ss
        else:
            out+=ss
        total-=ss
        if -1<yy+(move[dir][1])<N and -1<yy<N:
             board[yx][yy+(move[dir][1])]+=total
        else:
            out+=total

            
    elif dir==1 or dir==3:
        for i in range(2):
            nx=yx
            ny=yy+dx[i]
            ss=int(y_sand*(7/100))
            total-=ss
            if -1<nx<N and -1<ny<N:
                board[nx][ny]+=ss
            else:
                out+=ss
        for i in range(2):
            nx=yx+move[dir][0]
            ny=yy+dx[i]
            ss=int(y_sand*(10/100))
            total-=ss
            if -1<nx<N and -1<ny<N:
                board[nx][ny]+=ss
            else:
                # print(ss)
                out+=ss
        for i in range(2):
            nx=yx
            ny=yy+(dx[i]*2)
            ss=int(y_sand*(2/100))
            total-=ss
            if -1<nx<N and -1<ny<N:
                board[nx][ny]+=ss
            else:
                out+=ss
        for i in range(2):
            nx=x
            ny=y+dx[i]
            ss=int(y_sand*(1/100))
            total-=ss
            if -1<nx<N and -1<ny<N:
                board[nx][ny]+=ss
            else:
                out+=ss

        ss=int(y_sand*(5/100))
        if -1<yx+(move[dir][0]*2)<N and -1<yy<N:
            board[yx+(move[dir][0]*2)][yy]+=ss
        else:
            out+=ss
        total-=ss

        if -1<yx+(move[dir][0])<N and -1<yy<N:
             board[yx+(move[dir][0])][yy]+=total
        else:
            out+=total
    
    board[yx][yy]=0
            
        
        

            

def go(dir,n,x,y):
    for i in range(4):
        if i==dir:
            nx=x
            ny=y
            for j in range(n):
                sand(dir,nx,ny)
                nx=nx+(move[i][0])
                ny=ny+(move[i][1])                
                # pb(board)
            return [nx,ny]


def t_move(d,n,t,x,y):
    if x<=0 and y<=0:
        return
    if t==2:
        n+=1
        t=0
    if d==4:
        d=0
    tmp=go(d,n,x,y)
    t_move(d+1,n,t+1,tmp[0],tmp[1])


t_move(0,1,0,N//2,N//2)
print(out)


    

