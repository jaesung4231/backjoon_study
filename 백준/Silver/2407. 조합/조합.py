import sys
n,m=map(int,input().split())
top=n
down=m
for i in range(1,m):
    top*=(n-i)
for i in range(1,m):
    down*=(m-i)
print(top//down)
