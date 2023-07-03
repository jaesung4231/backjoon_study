import sys
input=sys.stdin.readline
n,m=map(int,input().split())
num=list(map(int,input().split()))

left=0
right=1
ans=0

while right<=n and left<=right:
    l=num[left:right]
    total=sum(l)
    if total==m:
        ans+=1
        right+=1
    elif total<m:
        right+=1
    else:
        left+=1
print(ans)
