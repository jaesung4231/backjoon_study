from collections import deque
from copy import deepcopy
import sys
input=sys.stdin.readline
M,N,K=map(int,input().split())
board=[]

def make_rec(s1,s2,e1,e2,N,M):
    hor_len=e1-s1
    var_len=e2-s2
    start_x=s2
    start_y=s1
    # print("var:",var_len,"hor:",hor_len,"start_x:",start_x,"start_y:",start_y)
    for i in range(var_len):
        for j in range(hor_len):
            board[start_x+i][start_y+j]=1

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    cnt=1
    board[x][y]=1
    queue=deque()
    queue.append([x,y])
    while(queue):
        a,b=queue.popleft()
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if -1<nx<M and -1<ny<N and board[nx][ny]==0:
                queue.append([nx,ny])
                board[nx][ny]=1
                cnt+=1
                
    return cnt

for i in range(M):
    board.append([0]*N)

for i in range(K):
    s1,s2,e1,e2=(map(int,input().split()))
    make_rec(s1,s2,e1,e2,N,M)

# for i in range(M):
#     print(board[i])


ans_num=0
ans_size=[]
for i in range(M):
    for j in range(N):
        if board[i][j]==0:
            ans_num+=1
            ans_size.append(bfs(i,j))
ans_size.sort()
print(ans_num)
print(*ans_size)

