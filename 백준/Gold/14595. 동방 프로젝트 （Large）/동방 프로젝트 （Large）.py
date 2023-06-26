from collections import deque, defaultdict
from itertools import combinations, product, permutations
from copy import deepcopy
import heapq
import sys
input=sys.stdin.readline
n=int(input())
m=int(input())
wall=[0]*(n)
act=[]

for i in range(m):
    act.append(list(map(int,input().split())))

if m>0:
    act.sort(key=lambda x:(x[0],x[1]))
    s=act[0][0]
    e=act[0][1]
    for i in range(1,m):
        if e<act[i][0]:
            for j in range(s,e):
                wall[j]=1
            s=act[i][0]
            e=act[i][1]
        else:
            e=max(e,act[i][1])
    for j in range(s,e):
        wall[j]=1

ans=1
for i in range(1,n):
    if wall[i]==0: ans+=1

print(ans)
