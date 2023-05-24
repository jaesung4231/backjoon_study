from itertools import combinations
from collections import deque
import math
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
number=[]
for i in  range(n):
    number.append(int(input()))
number.sort()
left=0
right=0
ans=2000000000
while left<n:
    cost=number[right]-number[left]
    if cost>=m:
        # print(left,right,cost)
        ans=min(ans,cost)
        left+=1
    else:
        right+=1
        if right>(n-1):
            break
print(ans)