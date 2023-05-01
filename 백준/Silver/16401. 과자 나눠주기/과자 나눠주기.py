from collections import deque, defaultdict
from itertools import combinations, product, permutations
from queue import PriorityQueue
from copy import deepcopy
import sys
import heapq
target,m=map(int,input().split())
num=list(map(int,input().split()))
num.sort()
ans=0
s=1
e=max(num)
cantDo=True

def check(x):
    cnt=0
    if x==0:
        return 0
    for i in num:
        cnt+=i//x
    return cnt

while(s<=e):
    mid=(s+e)//2
    canDo=check(mid)
    if canDo>=target:
        cantDo=False
        s=mid+1
        ans=max(ans,mid)
    elif canDo<target:
        e=mid-1

if cantDo==False:
    print(ans)
else:
    print(0)
