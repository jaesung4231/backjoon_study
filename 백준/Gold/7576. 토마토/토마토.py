from collections import deque
import sys
input=sys.stdin.readline
N,M=map(int,(input().split()))
##익으면 1 익지 않은 0 없음 -1
farm=[]
answer=[]
for i in range(M):
    farm.append(list(map(int,input().split())))
    answer.append([0]*N)

dx=[-1,1,0,0]
dy=[0,0,-1,1]
start=[]

def bfs(arr,answer,farm):
    queue=deque()
    for i in range(len(arr)):
        answer[arr[i][0]][arr[i][1]]=1
        queue.append(arr[i])
    
    while (queue):
        a,b=queue.popleft()
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if -1<nx<M and -1<ny<N and farm[nx][ny]==0:
                farm[nx][ny]=1
                queue.append([nx,ny])
                if answer[nx][ny]==0:
                    answer[nx][ny]=answer[a][b]+1
    
    return (answer[a][b]-1)


for i in range(M):
    for j in range(N):
        if farm[i][j]==1:
            start.append([i,j])
        elif farm[i][j]==(-1):
            answer[i][j]=(-1)
if len(start)==0:
    print(-1)
else:
    result=bfs(start,answer,farm)
    for i in range(M):
        if 0 in answer[i]:
            print(-1)
            break
        elif i==M-1:
            print(result)
        
