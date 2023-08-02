import sys
from collections import  deque
from itertools import combinations
input=sys.stdin.readline

n,m=map(int, input().split())
cow=list(map(int,input().split()))
prime=[0]*(max(cow)*n+1)
prime[0]=1
prime[1]=1

for i in range(len(prime)):
    if prime[i]==0:
        tmp=i*2
        while tmp<len(prime):
            prime[tmp]=1
            tmp+=i

ans=set()
for c in combinations(cow,r=m):
    l=list(c)
    s=sum(l)
    if prime[s]==0:
        ans.add(s)
    
ans=list(ans)
ans.sort()
if len(ans)!=0:
    print(*ans)
else:
    print(-1)