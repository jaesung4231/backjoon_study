from collections import deque
import copy
import sys
input=sys.stdin.readline
N,M=map(int,(input().split()))
##익으면 1 익지 않은 0 없음 -1
maze=[]
J_maze=[]
F_maze=[]

for i in range(N):
    maze.append(list(input().strip()))
    J_maze.append([0]*M)
    F_maze.append([0]*M)

dx=[-1,1,0,0]
dy=[0,0,-1,1]
J=[]
F=[]
result=[]


def bfs_F(F,maze):
    queue_F=deque()
    for i in F:
        queue_F.append(i)
        F_maze[i[0]][i[1]]=1
    while queue_F:
        fx,fy=queue_F.popleft()
        for i in range(4):
            fx_n=fx+dx[i]
            fy_n=fy+dy[i]
            if -1<fx_n<N and -1<fy_n<M and maze[fx_n][fy_n]=='.':
                maze[fx_n][fy_n]='F'
                queue_F.append([fx_n,fy_n]) 
                if F_maze[fx_n][fy_n]==0:
                    F_maze[fx_n][fy_n]=F_maze[fx][fy]+1


def bfs_J(J,maze):
        queue_J=deque()
        queue_J.append([J[0][0],J[0][1]])
        J_maze[J[0][0]][J[0][1]]=1
        while queue_J:
            jx,jy=queue_J.popleft()
            for i in range(4):
                jx_n=jx+dx[i]
                jy_n=jy+dy[i]  
                if -1<jx_n<N and -1<jy_n<M and maze[jx_n][jy_n]=='.':
                    maze[jx_n][jy_n]='J'
                    queue_J.append([jx_n,jy_n])
                    J_maze[jx_n][jy_n]=J_maze[jx][jy]+1
            
          
for i in range(N):
    for j in range(M):
        if maze[i][j]=='F':
            F.append([i,j])
        elif maze[i][j]=='J':
            J.append([i,j])

J_map=copy.deepcopy(maze)
F_map=copy.deepcopy(maze)
bfs_J(J,J_map)
bfs_F(F,F_map)
cnt=0
result=[]
sear=[0,0,N-1,M-1]
for i in range(N):
    for j in range(M):
        if i==0 or i==N-1 or j==0 or j==M-1:
            if J_maze[i][j]!=0 and (J_maze[i][j]<F_maze[i][j]):
                result.append(J_maze[i][j])
            elif J_maze[i][j]!=0 and F_maze[i][j]==0:
                result.append(J_maze[i][j])
            
if len(result)==0:
    print("IMPOSSIBLE")
else:
    print(min(result))

# for i in range(N):
#     print(*J_maze[i])
# print("================")
# for i in range(N):
#     print(*F_maze[i])
