from collections import deque, defaultdict
from itertools import combinations, product, permutations
from copy import deepcopy
import heapq
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
tree=list(map(int,input().split()))
left=0
right=2000000000
ans=0

def check(k):
    total=0
    for t in tree:
        if t>k:
            total+=(t-k)
    return total

while left<=right:
    mid=(left+right)//2
    total=check(mid)
    if total>=m:
        ans=max(ans,mid)
        left=mid+1
    elif total<m:
        right=mid-1

print(ans)