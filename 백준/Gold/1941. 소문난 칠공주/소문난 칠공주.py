from collections import deque, defaultdict
from itertools import permutations, combinations
import sys
input=sys.stdin.readline

board=[]
visited=[]
dx=[-1,1,0,0]
dy=[0,0,1,-1]
pos=[(i,j) for i in range(5) for j in range(5)]
combi=list(combinations(pos,7))
ans=0

for i in range(5):
    board.append(list(input().strip()))
    visited.append([0]*5)

def check_Y(arr):
    cnt=0
    for p in arr:
        if board[p[0]][p[1]]=='Y':
            cnt+=1
    if cnt>=4:
        return False
    return True

def dfs_Near(arr,k,table):
    x=arr[k][0]
    y=arr[k][1]
    table[x,y]=1
    cnt=1
    queue=deque()
    queue.append([x,y])
    while queue:
        a,b=queue.popleft()
        if cnt==7:
            return True
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if (nx,ny) in arr and (nx,ny) not in table:
                table[(nx,ny)]=1
                queue.append([nx,ny])
                cnt+=1
    return False
            
            

for princess in combi:
    if check_Y(princess):
        table={}
        if dfs_Near(princess,0,table):
            ans+=1

print(ans)





    
    
    



    



