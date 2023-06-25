from collections import deque, defaultdict
from itertools import combinations, product, permutations
from copy import deepcopy
import heapq
import sys
input=sys.stdin.readline
n,c=map(int,input().split())
weight=list(map(int,input().split()))
weight.sort()
two=defaultdict(int)
ans=0
for i in range(n):
    two[weight[i]]


if c in two:
    ans=1
else:
    left=0
    right=n-1
    while left<=right:
        mid=(left+right)//2
        w=weight[mid]
        if w==c:
            ans=1
            break
        if w>c:
            right=mid-1
        else:
            left=mid+1
    
    
    if ans==0:
        left=0
        right=n-1
        while left<right:
            total=weight[left]+weight[right]
            if total==c:
                ans=1
                break
            if total>c:
                right-=1
            else:
                diff=c-total
                if diff!=weight[left] and diff!=weight[right] and (diff in two):
                    ans=1
                    break
                left+=1

print(ans)
 
        
