import sys
input=sys.stdin.readline
t =int(input())
day=[]
price=[]
dp=[0]*(t+1)

for i in range(t):
    n,m=map(int,input().split())
    day.append(n)
    price.append(m)
M=0
for i in range(t):
    M=max(M,dp[i])
    if (day[i]+i)>t:
        continue
    dp[day[i]+i]=max(M+price[i],dp[day[i]+i])
    

print(max(dp))