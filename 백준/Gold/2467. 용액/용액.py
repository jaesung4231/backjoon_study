import sys
input=sys.stdin.readline
n=int(input())
number=list(map(int,input().split()))
number.sort()
left=0
right=n-1
ans_left=0
ans_right=0
ans=10000000000
while left<right:
    total=(number[left]+number[right])
    if total==0:
        ans_left=number[left]
        ans_right=number[right]
        break

    if total>0:
        if abs(total)<ans:
            ans=abs(total)
            ans_left=number[left]
            ans_right=number[right]
        right-=1

    elif total<0:
        if abs(total)<ans:
            ans=abs(total)
            ans_left=number[left]
            ans_right=number[right]
        left+=1

print(ans_left,ans_right)