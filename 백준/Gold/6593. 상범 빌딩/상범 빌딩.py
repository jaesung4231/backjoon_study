import sys
import copy
from copy import deepcopy
from collections import deque
N=[1,1,1]

Area=[]



def bfs(i,j):
    dx=[1,-1,0,0,(N[1]+1),-(N[1]+1)]
    dy=[0,0,1,-1,0,0]
    isEscape = False
    answer=0
    queue=deque()
    queue.append([i,j])
    Area[i][j]=0
    while (queue):
        a,b=queue.popleft()
        for i in range(6):
            nx=a+dx[i]
            ny=b+dy[i] 
            if -1<nx<floor and -1<ny<N[2] and (Area[nx][ny]=='.' or Area[nx][ny]=='E'):         
                if(Area[nx][ny]=='E'):
                    isEscape=True
                    answer=Area[a][b]+1
                queue.append([nx,ny])
                Area[nx][ny]=Area[a][b]+1


    if (isEscape):
        print(f"Escaped in {answer} minute(s).")
    else:
        print("Trapped!")



while(N[0]!=0 and N[1]!=0 and N[2]!=0):
    N= list(map(int,sys.stdin.readline().split()))
    ans=[]
    floor=(N[0]*N[1])+(N[0])
    for i in range(floor):
        data=(list(sys.stdin.readline().strip()))
        if len(data)==0:
            Area.append([0]*N[2])
        else:
            Area.append(data)

    for i in range(floor):
        for j in range(len(Area[i])):
            if(Area[i][j]=='S'):
                bfs(i,j)
    Area=[]
        
# print(Area)