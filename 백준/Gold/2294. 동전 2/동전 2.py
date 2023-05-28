import sys
import heapq
from collections import deque, defaultdict
from itertools import permutations, combinations, product, combinations_with_replacement
input=sys.stdin.readline
n,k=map(int,input().split())
number=[]
dp=[1e9]*(k+1)

for _ in range(n):
    a=int(input())
    number.append(a)

for i in number:
    for j in range(i,k+1):
        if j%i==0:
            dp[j]=min(dp[j],j//i)
        dp[j]=min(dp[j],dp[j-i]+dp[i])


if dp[k]!=1e9:
    print(dp[k])
else:
    print(-1)
