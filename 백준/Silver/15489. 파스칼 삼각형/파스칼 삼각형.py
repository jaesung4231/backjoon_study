import sys
from collections import deque
input=sys.stdin.readline
pyramid=[[1],[1,1]]
for i in range(2,30):
    floor=[1]
    for j in range(len(pyramid[i-1])-1):
        floor.append(pyramid[i-1][j]+pyramid[i-1][j+1])
    floor.append(1)
    pyramid.append(floor)


R,C,W=map(int,input().split())
ans=0
for i in range(W):
    for j in range(i+1):
        ans+=(pyramid[R+i-1][C+j-1])

print(ans)