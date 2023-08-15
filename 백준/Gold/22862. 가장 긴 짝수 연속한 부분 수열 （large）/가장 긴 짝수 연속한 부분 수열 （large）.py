import sys
from collections import deque
input=sys.stdin.readline
N,K=map(int,input().split())
S=list(map(int,input().split()))
left=0
right=0

cur=0
length=0
ans=0

while right<N and left<=right:
    if S[right]%2!=0 and cur<K:
        cur+=1
        right+=1
    
    elif S[right]%2!=0 and cur==K:
        if S[left]%2!=0:
            cur-=1
        else:
            length-=1
        left+=1
    
    elif S[right]%2==0:
        length+=1
        right+=1
    
    ans=max(length,ans)

print(ans)