import sys
from collections import deque
input=sys.stdin.readline
N=int(input())
path=list(input().strip())
dp=[1e9]*N

def find(cur):
    if cur=="B":
        return "J"
    elif cur=="O":
        return "B"
    elif cur=="J":
        return "O"

dp[0]=0
for i in range(N):
    k=find(path[i])
    for j in range(i):
        if path[j]==k:
            dp[i]=min(dp[i],dp[j]+pow(i-j,2))

if dp[N-1]>=1e9:
    print(-1)
else:
    print(dp[N-1])


