import sys
input=sys.stdin.readline
n,s,m=map(int,input().split())
volume=list(map(int,input().split()))
dp=[[0]*(m+1) for _ in range(n+1)]
dp[0][s]=1
ans=-1

for i in range(n):
    for j in range(m+1):
        if dp[i][j]==1:
            cost_up=j+volume[i]
            cost_down=j-volume[i]
            if cost_up<=m:
                dp[i+1][cost_up]=1
            if cost_down>=0:
                dp[i+1][cost_down]=1

for i in range(m,-1,-1):
    if dp[n][i]==1:
        ans=i
        break

print(ans)