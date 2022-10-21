from collections import deque
from copy import deepcopy
import sys
input=sys.stdin.readline
N=int(input())
dp=[0]*10000
dp[1]=1
dp[2]=2
dp[3]=3
for i in range(4,10000):
    dp[i]=((dp[i-1]+dp[i-2])%10007)
print(dp[N])