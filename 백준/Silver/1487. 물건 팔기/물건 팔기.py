from collections import deque, defaultdict
from itertools import combinations, product, permutations
from copy import deepcopy
import heapq
import sys
input=sys.stdin.readline
n=int(input())
price=[]
tax=[]
for i in range(n):
    a,b=map(int,input().split())
    price.append([a,b])

price.sort()
ans=0
buy=[]
answer=0

for i in range(n):
    cur=price[i][0]
    total=0
    for j in range(n):
        cost=cur-price[j][1]
        if price[j][0]>=cur and cost>0:
            total+=cost
    if total>ans:
        ans=total
        answer=cur

print(answer)



