from collections import deque
from copy import deepcopy
import sys 
input=sys.stdin.readline
n,m=map(int,input().split())
ice=[]
iceCopy=[]

for i in range(n):
    ice.append(list(map(int,input().split())))
    iceCopy.append([0]*m)

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def printIce():
    for i in range(n):
        print(ice[i])
    print("=====================")

def bfs(x,y):
    iceCopy=[]
    for i in range(n):
        iceCopy.append([0]*m)
    queue=deque()
    queue.append([x,y])
    iceCopy[x][y]=ice[x][y]
    while queue:
        a,b=queue.popleft()
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if -1<nx<n and -1<ny<m:
                if ice[nx][ny]==0 and iceCopy[nx][ny]==0 and ice[a][b]>0:
                    ice[a][b]-=1
                if  ice[nx][ny]!=0 and iceCopy[nx][ny]==0:
                    queue.append([nx,ny])
                    iceCopy[nx][ny]=ice[nx][ny] 
    # printIce() 

def bfs_check(x,y):
    queue=deque()
    queue.append([x,y])
    visited[x][y]=1
    while queue:
        a,b=queue.popleft()
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if ice[nx][ny]!=0 and visited[nx][ny]==0:
                queue.append([nx,ny])
                visited[nx][ny]=1
    

isTrue=True
time=0
while(isTrue):
    isTrue=False
    visited=[]
    result=[]
    iceNum=0
    for i in range(n):
        visited.append([0]*m)
    for i in range(n):
        for j in range(m):
            if ice[i][j]!=0 and visited[i][j]==0:
                bfs_check(i,j)
                iceNum+=1
                result.append([i,j])    
    # printIce()
    # print(iceNum,time)
    if iceNum==0:
        time=0
        isTrue-False
    if iceNum<2 and len(result)!=0:
        bfs(result[0][0],result[0][1])
        time+=1
        isTrue=True
    if iceNum>=2:
        isTrue=False
   
  
print(time)
              
            

   


            
         
            
            


                

          
            
