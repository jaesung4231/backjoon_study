import sys
import heapq
from collections import deque
from itertools import combinations
input=sys.stdin.readline
N,K=map(int,input().split())
height=list(map(int,input().split()))

dif=[]
for i in range(N-1):
    dif.append(abs(height[i]-height[i+1]))
dif.sort()
ans=sum(dif)
tmp=len(dif)-1
for i in range(K-1):
    ans-=dif[tmp]
    tmp-=1
print(ans)