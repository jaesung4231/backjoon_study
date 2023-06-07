import sys
import math
n,m=map(int,input().split())
board=[]
ans=-1
for i in range(n):
    board.append(list(input().strip()))

def ssqrt(num):
    s=int(num)
    if int(s**0.5)**2==s:
        return True
    return False


def check(x,y):
    global ans
    for i in range(-n,n):
        for j in range(-m,m):
            nx=x
            ny=y
            num=""
            if i==0 and j==0:
                continue
            while -1<nx<n and -1<ny<m:
                num+=(board[nx][ny])
                nx+=i
                ny+=j
                if ssqrt(num)==True:
                    ans=max(ans,int(num))


for i in range(n):
    for j in range(m):
        check(i,j)

print(ans)