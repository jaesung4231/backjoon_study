import sys
from collections import deque
input=sys.stdin.readline
N=int(input())
num=list(map(int,input().split()))
dp=num[:]
for i in range(N):
    for j in range(i):
        if num[j]>num[i]:
            dp[i]=max(dp[i],dp[j]+num[i])


print(max(dp))