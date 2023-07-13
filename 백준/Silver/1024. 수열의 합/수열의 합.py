from itertools import permutations
from collections import deque, defaultdict
import sys
input=sys.stdin.readline
n,l=map(int,(input().split()))

def binary_search(l):
    left=0
    right=n
    while left<=right:
        mid=(right+left)//2
        cost=mid*l
        for i in range(l):
            cost+=i

        if cost==n:

            return mid
        elif cost>n:
            right=mid-1
        elif cost<n:
            left=mid+1
    
    return -1

didFind=False

for i in range(l,101):
    ans=binary_search(i)
    if ans==-1:
        continue
    else:
        start=[s for s in range(ans,ans+i)]
        print(*start)
        didFind=True
        break

if not didFind:
    print(-1)