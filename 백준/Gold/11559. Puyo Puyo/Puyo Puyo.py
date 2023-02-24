from collections import deque, defaultdict
from copy import deepcopy
from itertools import permutations, combinations, product
import sys
input=sys.stdin.readline
# n,m=map(int,input().split())
board=[]
n=12 
m=6

dx=[-1,1,0,0]
dy=[0,0,1,-1]

def pb(board):
    for i in range(n):
        print(board[i])


for i in range(n):
    board.append(list(input().strip()))

visit=defaultdict(int)

def bfs(x,y):
    queue=deque()
    stack=[]
    queue.append([x,y])
    stack.append([x,y])
    cnt=1
    visited=defaultdict(int)
    visited[x,y]
    while(queue):
        a,b=queue.popleft()
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if -1<nx<n and -1<ny<m and board[nx][ny]==board[a][b]:
                if (nx,ny) not in visited:
                    queue.append([nx,ny])
                    stack.append([nx,ny])
                    visited[nx,ny]
                    cnt+=1
    if cnt>=4:
        for i in stack:
            board[i[0]][i[1]]='.'
        return True
    return False

def move():
    for i in range(6):
        for j in range(11,-1,-1):
            if board[j][i]=='.':
                for k in range(j,-1,-1):
                    if board[k][i]!='.':
                        board[j][i]=board[k][i]
                        board[k][i]='.'
                        break
        
        
ans=0
def check():
    global ans
    didpop=False
    for i in range(n):
        for j in range(m):
            if board[i][j]!='.':
                if bfs(i,j):
                    didpop=True

    if didpop==False:
        return ans
    else:
        ans+=1
        move()
        check()
        
check()
# pb(board)
print(ans)
