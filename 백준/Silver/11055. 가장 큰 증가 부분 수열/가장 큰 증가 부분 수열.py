import sys
input=sys.stdin.readline
n = int(input())
number = list(map(int, input().split()))
dp=[0]*n
dp[0]=number[0]

for i in range(1,n):
   for j in range(i):
    m=-1
    if number[j]<number[i]:
        dp[i]=max(dp[i],dp[j]+number[i])
    else:
        dp[i]=max(dp[i],number[i])
  

print(max(dp))