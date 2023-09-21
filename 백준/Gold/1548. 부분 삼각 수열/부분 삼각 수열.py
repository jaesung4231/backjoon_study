import sys
from itertools import combinations
input=sys.stdin.readline
N=int(input())
num=list(map(int,input().split()))
num.sort()

if N>2:
    ans=2
    for i in range(N-1):
        cost=num[i]+num[i+1]
        for j in range(i+2,N):
            if cost>num[j]:
                ans=max(ans,j-i+1)
            else: break
    
    print(ans)
else:
    print(N)


