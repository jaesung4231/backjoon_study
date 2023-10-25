import sys
import math
from collections import deque
from itertools import combinations
N,M=map(int,input().split())
switch=[set() for _ in range(N)]
for i in range(N):
    tmp=list(map(int,input().split()))
    for j in range(1,len(tmp)):
        switch[i].add(tmp[j])

canMake=0

for combi in combinations(range(N),r=N-1):
    button=[0]*(M+1)
    for c in combi:
        for sw in switch[c]:
            button[sw]=1
    if button.count(1)>=M:
        canMake=1
        break

print(canMake)