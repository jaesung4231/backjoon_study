import sys
from collections import defaultdict
input=sys.stdin.readline
stone=[]
N=int(input())
dp=[[1e9]*(N) for _ in range(N)]
dis=[]


for i in range(N-1):
    a,b=map(int,input().split())
    stone.append([a,b])

for i in range(N):
    dp[i][0]=0

K=int(input())
if N==1:
    print(0)
else:
    for i in range(N-1):
        for j in range(N):
            if i==j-3 and -1<j-3:
                dp[i][j]=min(dp[i][j],dp[i][j-1]+stone[j-1][0],dp[i][j-2]+stone[j-2][1],dp[i][j-3]+K)
            elif -1<j-2:
                dp[i][j]=min(dp[i][j],dp[i][j-1]+stone[j-1][0],dp[i][j-2]+stone[j-2][1])
            else:
                dp[i][j]=min(dp[i][j],dp[i][j-1]+stone[j-1][0])
        dis.append(dp[i][N-1])
    print(min(dis))
 
