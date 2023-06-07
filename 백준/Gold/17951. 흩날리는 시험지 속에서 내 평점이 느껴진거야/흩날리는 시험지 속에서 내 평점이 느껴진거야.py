import sys
from collections import defaultdict
input=sys.stdin.readline
n,k=map(int,input().split())
test=list(map(int,input().split()))
left=0
right=int(1e5)*20+1
ans=0

while left<=right:
    mid=(left+right)//2
    group=0
    score=0
    for t in test:
        score+=t
        if score>=mid:
            group+=1
            score=0
    if group >= k:
        ans=mid
        left=mid+1
    else:
        right=mid-1

print(ans)
