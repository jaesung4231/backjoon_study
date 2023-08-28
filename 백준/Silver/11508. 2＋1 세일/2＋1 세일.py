import sys
from collections import deque
input=sys.stdin.readline
dairy=[]
N=int(input())
for _ in range(N):
    dairy.append(int(input()))

dairy.sort()
ans=0
cur=1
for i in range(N-1,-1,-1):
    if cur%3==0:
        cur+=1 
        continue
    ans+=dairy[i]
    cur+=1
print(ans)