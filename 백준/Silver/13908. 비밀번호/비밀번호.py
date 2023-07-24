import sys
from itertools import permutations
input=sys.stdin.readline
n,m=map(int,input().split())
num=list(map(int,input().split()))

cnt=0
for i in range((10**n)):
    tmp=str(i)
    tmp=(tmp.zfill(n))
    isthere=True
    for j in num:
        if str(j) not in tmp:
            isthere=False
            break
    if isthere:
        # print(i,"i")
        cnt+=1

print(cnt)