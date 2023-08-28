import sys
input=sys.stdin.readline
N=int(input())
solution=list(map(int,input().split()))
left=0
right=N-1

ans=200000001
while left<right :
    cost=(solution[right])+(solution[left])
    
    if abs(cost)<abs(ans):
        ans=cost

    if cost==0:
        break
    elif cost<0:
        left+=1
    elif cost>0:
        right-=1 

print(ans)