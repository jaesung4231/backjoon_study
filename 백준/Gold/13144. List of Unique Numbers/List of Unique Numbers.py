import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
num=list(map(int,input().split()))
left=0
right=0
ans=0
idx=[0]*100001

while right<n:
    k=idx[num[right]]
    # print(p,left,right)
    if k==0:
        idx[num[right]]=1
        right+=1
        ans+=(right-left)
    else:
        idx[num[left]]=0
        left+=1

print(ans)