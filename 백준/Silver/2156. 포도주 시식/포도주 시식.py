from collections import deque, defaultdict
from itertools import combinations, product, permutations
from copy import deepcopy
import sys
input=sys.stdin.readline
grape=[]
n=int(input())
dp=[0]*n
for i in range(n):
    grape.append(int(input()))

dp[0]=grape[0]
if n>=2:
    dp[1]=grape[0]+grape[1]
if n>=3:
    dp[2]=max(dp[1],grape[1]+grape[2],grape[0]+grape[2])


for i in range(3,n):
    dp[i]=max(dp[i-1],grape[i]+dp[i-2],grape[i]+grape[i-1]+dp[i-3])

print(max(dp))