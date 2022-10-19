from collections import deque
from copy import deepcopy
import sys
input=sys.stdin.readline
N=int(input())
dp=[0]*100
dp[1]=1 
dp[2]=2
dp[3]=4


for i in range(4,12):
    dp[i]=dp[i-1]+dp[i-2]+dp[i-3]


for i in range(N):
    print(dp[int(input())])

