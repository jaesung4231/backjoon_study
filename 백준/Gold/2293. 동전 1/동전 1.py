import sys
import heapq
from collections import deque, defaultdict
from itertools import permutations, combinations, product, combinations_with_replacement
input=sys.stdin.readline
n,m=map(int,input().split())
number=[]
dp=[0]*(m+1)
dp[0]=1
for _ in range(n):
    number.append(int(input()))
for i in number:
    for j in range(i,m+1):
        dp[j]+=dp[j-i]

    
print(dp[m])
