import sys
input=sys.stdin.readline
dp=[]
n=int(input())

dp=[True,False,True]
for i in range(3,1001):
    if dp[i-1]==True and dp[i-3]==True:
        dp.append(False)
    else:
        dp.append(True)

if dp[n-1]==True:
    print("SK")
else:
    print("CY")
