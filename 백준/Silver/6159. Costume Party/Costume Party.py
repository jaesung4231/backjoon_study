import sys
from itertools import combinations
input=sys.stdin.readline
n,s=map(int,input().split())
weight=[]
for i in range(n):
    weight.append(int(input()))

ans=0

for i in range(n):
    for j in range(i+1,n):
        cost=weight[i]+weight[j]
        if cost<=s:
            ans+=1

print(ans)