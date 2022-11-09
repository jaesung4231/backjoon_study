from collections import deque
from copy import deepcopy
import sys
input=sys.stdin.readline
board=[]


data=list(map(int,(input().split())))
building=[0]*data[0]
dx=[data[3],-(data[4])]

def bfs(x):
    building[x]=1
    queue=deque()
    queue.append(x)
    while(queue):
        a=queue.popleft()
        for i in range(2):
            nx=a+dx[i]
            if -1<nx<data[0] and building[nx]==0:
                queue.append(nx)
                building[nx]=building[a]+1

bfs(data[1]-1)
# print(building)
if (building[data[2]-1])== 0:
    print("use the stairs")
else:
    print(building[data[2]-1]-1)

