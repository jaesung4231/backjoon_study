# from collections import deque
# from copy import deepcopy
import sys 
input=sys.stdin.readline

t=int(input())


def func(n):
    if n==0 or n==1:
        print(*dp[n])
        return
    for i in range(2,n+1):
        dp[i][0]=dp[i-1][0]+dp[i-2][0]
        dp[i][1]=dp[i-1][1]+dp[i-2][1]
    print(*dp[n])


for i in range(t):
    n=int(input())
    dp=[[0,0] for _ in range(n+2)]
    dp[0][0]=1
    dp[0][1]=0
    dp[1][0]=0
    dp[1][1]=1
    func(n)

            
         
            
            


                

          
            
