import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
m=int(input())
lamp=list(map(int,input().split()))
ans=1e9
def check(h):
    tmp=[]
    for l in lamp:
        tmp.append([l-h,l+h])   
    if tmp[0][0]>0:
        return False
    elif tmp[len(tmp)-1][1]<n:
        return False
    else:
        for i in range(1,len(tmp)):
            if tmp[i][0]>tmp[i-1][1]:
                return False
        return True

left=0
right=n

while left<=right:
    mid=(left+right)//2
    r=check(mid)
    if r:
        right=mid-1
        ans=min(ans,mid)
    else:
        left=mid+1
    
print(ans)


