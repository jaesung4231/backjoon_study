from collections import deque
from copy import deepcopy
import sys
input=sys.stdin.readline
T=int(input())

cb=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(F,S,maze,ans):
    queue=deque()
    tmp=[]
    for i in F:
        queue.append([i[0],i[1]])
        ans[i[0]][i[1]]=1
    queue.append([S[0],S[1]])
    ans[S[0]][S[1]]=1
    while(queue):
        a,b=queue.popleft()
        cur=maze[a][b]
        if cur=="@" and (a==0 or a==M-1 or b==0 or b==N-1):
                tmp.append(ans[a][b])
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if -1<nx<M and -1<ny<N and maze[nx][ny]=='.':
                maze[nx][ny]=cur
                queue.append([nx,ny])
                if ans[nx][ny]==0:
                    ans[nx][ny]=ans[a][b]+1
                if cur=="@" and (nx==0 or nx==M-1 or ny==0 or ny==N-1):
                    tmp.append(ans[nx][ny])
    
    if len(tmp)==0:
        print("IMPOSSIBLE")
        return 
    else:
        print(min(tmp))
        return 

for i in range(T):
    N,M=map(int,input().split())
    maze=[]
    ans=[]
    dis=[]
    F=[]
    for j in range(M):
        maze.append(list(input().strip()))
        ans.append([0]*N)
    for j in range(M):
        for k in range(N):
            if maze[j][k]=='*':
                F.append([j,k])
            elif maze[j][k]=="@":
                S=[j,k]

    bfs(F,S,maze,ans)
    # if dis[0]==None:
    #     print("IMPOSSIBLE")
    # else:
    #     print(min(dis))
   
