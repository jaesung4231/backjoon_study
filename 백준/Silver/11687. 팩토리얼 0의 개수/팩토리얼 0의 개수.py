import sys
from itertools import permutations
input=sys.stdin.readline
M=int(input())

def count(n):
    tmp=0
    while n>=5:
        tmp+=n//5
        n=n//5
    return tmp

left=1
right=M*5
ans=1e9

while left<=right:
    mid=(left+right)//2
    zero=count(mid)
    if zero>=M:
        if zero==M:
            ans=mid
        right=mid-1
    elif zero<M:
        left=mid+1


if ans==1e9:
    print(-1)
else:
    print(ans)
