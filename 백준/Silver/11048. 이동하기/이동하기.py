import sys
input=sys.stdin.readline
n,m=map(int,input().split())
candy=[]
dp=[[0]*m for _ in range(n)]
for _ in range(n):
    candy.append(list(map(int,input().split())))
dp[0][0]=candy[0][0]

for i in range(1,n):
    dp[i][0]=dp[i-1][0]+candy[i][0]

for i in range(1,m):
    dp[0][i]=dp[0][i-1]+candy[0][i]

for i in range(1,n):
    for j in range(1,m):
        dp[i][j]=max(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+candy[i][j]

print(dp[n-1][m-1])