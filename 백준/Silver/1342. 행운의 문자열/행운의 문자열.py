import sys
from itertools import permutations
input=sys.stdin.readline
cnt=0
W=list(map(str,input().strip()))
ans=set()
N=len(W)
for p in permutations(W,N):
    same=False
    tmp=""
    for i in range(N-1):
        tmp+=p[i]
        if p[i]==p[i+1]:
            same=True
            break
    tmp+=p[N-1]
    if not same:
        ans.add(tmp)

print(len(ans))