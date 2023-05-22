import sys
from collections import deque
input=sys.stdin.readline
n,m,A,B,k=map(int,input().split())
board=[]
visited=[]
move=[[0,0],[1,0],[0,1],[1,1]]
dx=[-1,1,0,0]
dy=[0,0,1,-1]
for i in range(n):
    board.append([0]*m)
    visited.append([0]*m)
for i in range(k):
    a,b=map(int,input().split())
    board[a-1][b-1]=2

a,b=map(int,input().split())
s=[a-1,b-1]
c,d=map(int,input().split())
e=[c-1,d-1]

def pb(board):
    for i in range(n):
        print(board[i])
    print("==============")


def check(s):
    for i in range(A):
        for j in range(B):
            # print(s[0]+i,s[1]+j,"A,B")
            x=s[0]+i
            y=s[1]+j
            if x<0 or x>=n or y<0 or y>=m or board[x][y]==2:
                return False 
            
    return True


def bfs(s):
    queue=deque()
    queue.append([s[0],s[1]])
    visited[s[0]][s[1]]=1
    if check(e)==False:
        return -1
    while(queue):
        a,b=queue.popleft()
        if [a,b]==e:
            return visited[a][b]
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if -1<nx<n and -1<ny<m and visited[nx][ny]==0:
                if check([nx,ny])==True:
                    if [nx,ny]==e:
                        return visited[a][b]
                    queue.append([nx,ny])
                    visited[nx][ny]=visited[a][b]+1
    return -1

print(bfs(s))
# check(s)
# pb(board)
# pb(visited)
