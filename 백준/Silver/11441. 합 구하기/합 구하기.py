import sys
import math
from collections import deque
from itertools import combinations
input=sys.stdin.readline
N=int(input())
num=[0]+list(map(int,input().split()))
dp=[0]*(N+1)
dp[1]=num[1]
for i in range(2,N+1):
    dp[i]=num[i]+dp[i-1]

M=int(input())
for i in range(M):
    a,b=map(int,input().split())
    print(dp[b]-dp[a-1])