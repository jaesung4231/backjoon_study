import sys
import math
from itertools import combinations
input=sys.stdin.readline

T=int(input())
for t in range(T):
    n,m=map(int,input().split())
    cnt=0
    for c in combinations(range(1,n),2):
        l=list(c)
        a=l[0]
        b=l[1]
        if (a**2+b**2+m)/(a*b)==(a**2+b**2+m)//(a*b): cnt+=1
    print(cnt)
