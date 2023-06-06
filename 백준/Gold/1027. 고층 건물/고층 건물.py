import sys
import heapq
from collections import deque, defaultdict
from itertools import permutations, combinations, product, combinations_with_replacement
n=int(input())
build=list(map(int,input().split()))
num=[0]*n

for i in range(n-1):
    lean=-1e9
    for j in range(i+1,n):
        angle=((build[j]-build[i])/(j-i))
        if angle>lean:
            lean=angle
            num[i]+=1
            num[j]+=1
    
print(max(num))
