import sys
from collections import defaultdict
input=sys.stdin.readline
n,m=map(int,input().split())
galaxy=[]
order=[]
for i in range(n):
    planets=list(map(int,input().split()))
    galaxy=planets[:]
    planets.sort()
    tmp=[]
    for p in galaxy:
        left=0
        right=m-1
        while left<=right:
            mid=(left+right)//2
            num=planets[mid]
            if p==num:
                tmp.append(mid)
                break
            elif num>p:
                right=mid-1
            elif num<p:
                left=mid+1
    order.append(tmp)

ans=0

def check(x,y):
    for i in range(m):
        if order[x][i]!=order[y][i]:
            return False
    return True

for i in range(n):
    for j in range(i,n):
        if i==j: continue
        if check(i,j)==True: ans+=1

    
print(ans)