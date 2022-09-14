import sys

def dp(N):
    arr=[0,1,1,1,2,2]
    if N>=6:
        for i in range(6,N+1):
            arr.append(arr[i-1]+arr[i-5])
    return arr[N]

for i in range(int(input())):
    print(dp(int(sys.stdin.readline())))