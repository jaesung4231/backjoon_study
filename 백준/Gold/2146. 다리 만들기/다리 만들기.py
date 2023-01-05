from collections import deque
# from copy import deepcopy
import sys 
input=sys.stdin.readline

n=int(input())
board=[]
visited=[]
island=[]
ans=[]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(n):
    board.append(list(input().split()))
    visited.append([0]*n)


def print_board():
    print("=======border======")
    for i in range(n):
        print(board[i])


def print_visited():
    print("======visited=======")
    for i in range(n):
        print(visited[i])


def bfs(island):
    # print("가장자리",island)
    queue=deque()

    for i in range(len(island)):
        visited[island[i][0]][island[i][1]]=1
        queue.append([island[i][0],island[i][1]])
    while queue:
        a,b=queue.popleft()
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if -1<nx<n and -1<ny<n:
                if board[nx][ny]=='0' and visited[nx][ny]==0:
                    queue.append([nx,ny])
                    visited[nx][ny]=visited[a][b]+1
                if board[nx][ny]=='1':
                    ans.append(visited[a][b]-1)
    
    # print_visited()
                
def border(i,j):
    queue=deque()
    queue.append([i,j])
    board[i][j]="w"
    while(queue):
        a,b=queue.popleft()
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if -1<nx<n and -1<ny<n:
                if board[nx][ny]=='1':
                    queue.append([nx,ny])
                    board[nx][ny]='w'
                if board[nx][ny]=='0' and ([a,b]) not in island:
                    island.append([a,b])
    
    # print_board()


for i in range(n):
    for j in range(n):
        if board[i][j]=="1":
            border(i,j)
            bfs(island)
            island=[]
            visited=[]
            for i in range(n):
                visited.append([0]*n)
print(min(ans))





                
                
