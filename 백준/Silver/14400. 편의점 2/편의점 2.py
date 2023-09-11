import sys
import math
from itertools import combinations
input=sys.stdin.readline
N=int(input())
comv=[]
for _ in range(N):
    a,b=map(int,input().split())
    comv.append([a, b])

a=sorted(comv, key=lambda x: x[0])[N//2][0]
b=sorted(comv, key=lambda x: x[1])[N//2][1]
total=0
for c in comv:
    total+=abs(c[0]-a)+abs(c[1]-b)
print(total)