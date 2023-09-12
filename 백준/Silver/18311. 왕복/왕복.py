import sys
import math
from itertools import combinations
input=sys.stdin.readline
N,K=map(int,input().split())
dis=list(map(int,input().split()))
path=[0]*(N+1)
for i in range(1,N+1):
    path[i]=path[i-1]+dis[i-1]

for i in range(N):
    path.append(path[-1]+dis[N-i-1])

track=[i for i in range(1,N+1)]+[i for i in range(N,0,-1)]

cur=0
for i in range(1,2*N):
    if path[i]<=K:
        cur+=1
    else:
        break
print(track[cur])