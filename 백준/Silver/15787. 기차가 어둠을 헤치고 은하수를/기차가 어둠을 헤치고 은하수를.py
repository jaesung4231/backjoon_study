import sys
from collections import deque
input=sys.stdin.readline
N,M=map(int,input().split())
train=deque()
for i in range(N):
    t=deque()
    for _ in range(20): t.append(0)
    train.append(t) 


def move(k):
    K=k[0]
    if K==1:
        train[k[1]-1][k[2]-1]=1
    
    elif K==2:
        train[k[1]-1][k[2]-1]=0
    
    elif K==3:
        train[k[1]-1].pop()
        train[k[1]-1].appendleft(0)
    
    elif K==4:
        train[k[1]-1].popleft()
        train[k[1]-1].append(0)


for _ in range(M):
    command=list(map(int,input().split()))
    move(command)

ans=set()
for tr in train:
    tmp=""
    for t in tr:
        tmp+=str(t)
    ans.add(tmp)

print(len(ans))