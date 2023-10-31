import sys
from collections import deque
input=sys.stdin.readline
N=int(input())
day=[0]
money=[0]
dp=[0]*(N+2)
for _ in range(N):
    a,b=map(int,input().split())
    day.append(a)
    money.append(b)
cur=0

for i in range(1,N+1):
    end=day[i]+i
    if end<=(N+1):
        cur=dp[i]+money[i]
        for j in range(end,N+2):
            dp[j]=max(cur,dp[j])
print(dp[N+1])