import sys
N=int(input())
result=[0]*20000000
data=list(map(int, sys.stdin.readline().split()))
for i in data:
    result[i+10000000]=1
M=int(input())
card=list(map(int, sys.stdin.readline().split()))
for i in card:
    print(result[i+10000000], end=' ')