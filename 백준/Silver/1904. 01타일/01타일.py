import sys
arr=[0]*1000001
N=int(input())
def dp(n):
    arr[0]=0
    arr[1]=1
    arr[2]=2
    if n>=3:
        for i in range(3,n+1):
            arr[i]=(arr[i-1]+arr[i-2])%15746
    return arr[n]

print(dp(N)%15746)