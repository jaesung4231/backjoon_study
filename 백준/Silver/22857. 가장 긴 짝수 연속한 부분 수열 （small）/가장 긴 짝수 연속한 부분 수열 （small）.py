import sys
from itertools import combinations
input=sys.stdin.readline
N,K=map(int,input().split())
S=list(map(int,input().split()))
left=0
right=0
delete=K
ans=0
if S[0]%2!=0:
    delete-=1

while left<=right and right<N:
    # print(left,right,delete)
    length=(right-left-(K-delete)+1)
    ans=max(length,ans)
    if delete==0:
        if right==N-1: break
        if S[right+1]%2==0:
            right+=1
        else:
            if S[left]%2!=0:
                delete+=1
            left+=1
    elif delete>0:
        if right==N-1: break
        right+=1
        if S[right]%2!=0:
            delete-=1
    else: 
        print("[ERROR]", left,right,delete)

print(ans)
    