from collections import deque, defaultdict
from copy import deepcopy
from itertools import permutations, combinations, product
import sys
input=sys.stdin.readline
gear=[]
start=[]
dx=[1,-1]
for i in range(4):
    gear.append(list(input().strip()))

k=int(input())

for i in range(k):
    start.append(list(map(int,input().split())))

def spin(idx,n):
    if n==1:
        tmp=gear[idx].pop()
        gear[idx].insert(0,tmp)

    elif n==-1:
        tmp=gear[idx].pop(0)
        gear[idx].append(tmp)

visited=[]

def check(x,y):
    visited[x]=1
    for i in range(2):
        nx=x+dx[i]
        if -1<nx<4 and visited[nx]==0:
            visited[nx]=1
            if dx[i]==-1 and gear[nx][2]!=gear[x][6]:
                check(nx,-y)
            elif dx[i]==1 and gear[x][2]!=gear[nx][6]:
                check(nx,-y)
    
    spin(x,y)




for i in range(k):
    visited=[0,0,0,0]
    check(start[i][0]-1,start[i][1])


ans=0
score=[1,2,4,8]
for i in range(4):
    if gear[i][0]=='1':
        ans+=score[i]

print(ans)