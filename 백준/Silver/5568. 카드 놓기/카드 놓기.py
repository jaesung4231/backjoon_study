import sys
import math
from itertools import permutations
input=sys.stdin.readline
n=int(input())
k=int(input())
card=[]
ans=set()
for i in range(n):
    a=input().strip()
    card.append(a)

for c in permutations(card,r=k):
    tmp=""
    for i in c:
        tmp+=i
    ans.add(tmp)

print(len(ans))
