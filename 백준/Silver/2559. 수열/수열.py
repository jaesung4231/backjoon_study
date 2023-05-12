from itertools import combinations
import sys
input=sys.stdin.readline
n,k=map(int,input().split())
number=list(map(int,input().split()))
total=0
cnt=0
ans=-1e9
for i in range(n):
    if i<k:
        total+=number[i]
    if i>=k:
        # print(i,k,total)
        ans=max(ans,total)
        total-=number[i-k]
        total+=number[i]
ans=max(ans,total)
print(ans)
