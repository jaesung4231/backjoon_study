import sys
input=sys.stdin.readline


n=int(input())
number=list(map(int,input().split()))
number.sort()
x=2e+9+1
left=0
right=n-1
ans_1=0
ans_2=0

while left < right:
    S=(number[right]+number[left])
    if abs(S)<x:
        x=abs(S)
        ans_1=number[left] 
        ans_2=number[right]  
    if S<0:
        left+=1
    else:
        right-=1

print(ans_1, ans_2)
    



