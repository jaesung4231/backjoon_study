import sys
input=sys.stdin.readline
n=int(input())
stair=[]
dp=[]
for i in range(n):
    stair.append(int(input()))

dp.append(0)
dp.append(stair[0])
if n>1:
    dp.append(stair[0]+stair[1])
for i in range(2,n):
    dp.append(max(dp[i-2]+stair[i]+stair[i-1],stair[i]+dp[i-1]))

print(dp[n])
