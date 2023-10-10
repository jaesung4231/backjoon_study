import sys
import math
from collections import deque, defaultdict
from itertools import combinations
N,M=map(int,input().split())
table=defaultdict(int)
for _ in range(N):
    table[input().strip()]
ans=0
for _ in range(M):
    word=input().strip()
    if word in table:
        ans+=1
print(ans)