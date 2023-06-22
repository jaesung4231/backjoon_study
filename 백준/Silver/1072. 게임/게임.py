import sys
import math
input=sys.stdin.readline
x,y=map(int,input().split())
def check(a):
    return int(((y+a)*100/(x+a)))

left=1
right=x
z=check(0)
ans=0

while left<=right:
    mid=(left+right)//2
    cost=(mid-y)
    cur=check(mid)
    if cur>z:
        ans=mid
        right=mid-1
    elif cur<=z:
        left=mid+1

if z>=99:
    print(-1)
else:
    print(ans)


