from collections import deque, defaultdict
from copy import deepcopy
from itertools import permutations, combinations, product
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
t=int(input())

box=[]
can=[m]*(n+1) 
for i in range(t):
    data=list(map(int,input().split()))
    box.append([data[0],data[1],data[2]])


box.sort(key=lambda x:x[1])
ans=0
for b in range(len(box)):
    mii=m
    for i in range(box[b][0], box[b][1]):
        mii=min(mii, can[i])
    mii=min(mii,box[b][2])

    for i in range(box[b][0],box[b][1]):
        can[i]-=mii
    ans+=mii

print(ans)



            




