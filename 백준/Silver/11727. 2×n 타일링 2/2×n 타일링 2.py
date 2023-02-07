from collections import deque, defaultdict
from copy import deepcopy
from itertools import permutations, combinations
import sys
input=sys.stdin.readline
board=[]
avail=[]
cnt=0
n=int(input())
# 1 1
# 2 3
# 3 5
# 4 11 
# 5        

dp=[0]*1001
dp[1]=1
dp[2]=3
dp[3]=5
for i in range(3,1001):
    dp[i]=dp[i-1]+dp[i-2]*2

print(dp[n]%10007)



