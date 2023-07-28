import sys
from itertools import combinations
input=sys.stdin.readline
n,s=map(int,input().split())
weight=[]
for i in range(n):
    weight.append(int(input()))

weight.sort()
left=0
right=n-1
ans=0

# 1 2 3 5

while left<=right:
    sum=weight[left]+weight[right]
    if sum<=s:
        ans+=(right-left)
        left+=1

    elif sum>s:
        right-=1

print(ans)
