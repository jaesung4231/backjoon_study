import sys
input=sys.stdin.readline

N,C=map(int,input().split())
wifi=[]
ans=0
for i in range(N):
    wifi.append(int(input()))

wifi.sort()

left=1
right=wifi[-1]-wifi[0]
while left<=right:
    mid=(left+right)//2
    cnt=1
    cur=wifi[0]
    for i in range(1,N):
        dis=wifi[i]-cur
        if dis>=mid:
            cur=wifi[i]
            cnt+=1
   
    if cnt>=C:
        ans=max(ans,mid)
        left=mid+1
    else:
        right=mid-1
    

print(ans)
        
