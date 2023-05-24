import sys
import math
from collections import defaultdict
from itertools import permutations
input=sys.stdin.readline
n,k=map(int,input().split())
left=0
right=n//2
cancut=False
while left<=right:
    row=(left+right)//2
    col=n-row
    pieces=(row+1)*(col+1)
    if pieces==k:
        print("YES")
        cancut=True
        break
    if k>pieces:
        left=row+1
    else:
        right=row-1

if cancut==False:
    print("NO")
    
