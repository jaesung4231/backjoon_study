from collections import deque, defaultdict
from copy import deepcopy
from itertools import permutations, combinations
import sys
input=sys.stdin.readline
n = int(input())
dp=[0]*n
day=[]
price=[]
for i in range(n):
    a,b=map(int,input().split())
    day.append(a)
    price.append(b)

if day[0]-1<n:
    dp[0]=price[0]
else:
    dp[0]=0

for i in range(n):
    if day[i]+i-1<n:
        for j in range(i):
            if day[j]+j-1<i:
                dp[i]=max(price[i]+dp[j], dp[i])
            else:
                dp[i]=max(price[i],dp[i])

print(max(dp))
