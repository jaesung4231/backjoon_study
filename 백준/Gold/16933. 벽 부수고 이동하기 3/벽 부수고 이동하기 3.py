from collections import deque
import sys
input=sys.stdin.readline

n,m,k=map(int,input().split())
board=[]
visited=[[[0]*(k+1) for _ in range(m)] for _ in range(n)]
stay=[]

dx=[1,-1,0,0,0]
dy=[0,0,1,-1,0]

def print_visited():
    for i in range(n):
        print(visited[i])
    print("================================")

def print_wall():
    for i in range(n):
        print(stay[i])
    print("================================")


for i in range(n):
     board.append(list(input().strip()))
     stay.append([0]*m)
    
def bfs(k):
    visited[0][0][k]=1
    queue=deque()
    queue_2=deque()
    queue_3=deque()
    queue.append([0,0,k,True])
    time=0
    while queue:
        while(queue):
            a,b,c,d=queue.popleft()
            if a==n-1 and b==m-1:
                print(visited[a][b][c])
                return
            for i in range(4):
                nx=a+dx[i]
                ny=b+dy[i]
                if -1<nx<n and -1<ny<m:
                    if board[nx][ny]=='0' and visited[nx][ny][c]==0:
                        queue_2.append([nx,ny,c,not d])
                        visited[nx][ny][c]=visited[a][b][c]+1
        
                    if c>0 and board[nx][ny]=='1' and visited[nx][ny][c-1]==0:
                        if d==True:
                            queue_2.append([nx,ny,c-1, not d])
                            visited[nx][ny][c-1]=visited[a][b][c]+1
                        
                        if d==False:
                            queue_3.append([nx,ny,c-1,d])
                            visited[nx][ny][c-1]=visited[a][b][c]+2
        queue,queue_2,queue_3=queue_2,queue_3, deque()
        if not queue:
            queue,queue_2=queue_2,deque()
                
    print(-1)
                
bfs(k)









