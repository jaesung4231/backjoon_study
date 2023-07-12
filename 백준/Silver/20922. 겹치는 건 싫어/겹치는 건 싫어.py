import sys
input=sys.stdin.readline
n,k=map(int,input().split())
number=list(map(int,input().split()))
idx=[0]*100001
left=0
right=0
idx[number[left]]=1
cur=idx[number[right]]
length=1
ans=1

while right<n or left<right:
    cur=idx[number[right]]
    # print(right,left)
    if cur>k:
        idx[number[left]]-=1
        left+=1
        length-=1
    elif cur<=k:
        ans=max(length,ans)
        if right<n-1:
            right+=1
            idx[number[right]]+=1
            length+=1
        else:
            break


print(ans)
    
    

