from collections import deque, defaultdict
from copy import deepcopy
from itertools import permutations, combinations
import sys
input=sys.stdin.readline
board=[]
n,m,k,t=map(int,input().split())
spot=defaultdict(int)

dx=[-1,1,0,0]
dy=[0,0,1,-1]

for i in range(n):
    board.append(list(map(str,input().split())))


def print_board(board):
    for i in range(n):
        print(board[i])
    print("===================")

for i in range(n):
    for j in range(m):
        if board[i][j]=='2':
            spot[i,j]


def bfs(g,r,board,map):
    flower=0
    queue=deque()
    # print_board(map)
    for i in g:
        queue.append([i[0],i[1]])
    for j in r:
        queue.append([j[0],j[1]])

    while queue:
        a,b=queue.popleft()
        if board[a][b]=='f':
            continue
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if -1<nx<n and -1<ny<m:
                if board[a][b]=='g':
                    if board[nx][ny]=='1' or board[nx][ny]=='2':
                        board[nx][ny]=board[a][b]
                        queue.append([nx,ny])
                elif board[a][b]=='r':
                    if board[nx][ny]=='g':
                        board[nx][ny]='f'
                        flower+=1
                    if board[nx][ny]=='1' or board[nx][ny]=='2':
                        board[nx][ny]=board[a][b]
                        queue.append([nx,ny])
        board[a][b]='x'
      
        # print_board(board)
    return flower


    
ans=-1

for i in combinations(spot,k):
    green=defaultdict(int)
    combo_red=defaultdict(int)
    for a in i:
        spot[a]=1
        green[a]
        board[a[0]][a[1]]="g"

    for k in spot:
        if spot[k]==0:
            combo_red[k]

    for j in combinations(combo_red,t):
        red=defaultdict(int)
        for l in j:
            board[l[0]][l[1]]="r"
            red[l]
        ans=max(ans,bfs(green,red,deepcopy(board),board))
        for l in j:
            board[l[0]][l[1]]='2'
    
    for a in i:
        spot[a]=0
        board[a[0]][a[1]]="2"
        

print(ans)


