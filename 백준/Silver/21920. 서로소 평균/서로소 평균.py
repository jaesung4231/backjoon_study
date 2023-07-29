import sys
input=sys.stdin.readline

def gcd(a,b):
    while b>0:
        a,b=b,a%b
    return a

n=int(input())
A=list(map(int,input().split()))
X=int(input())

total=0
cnt=0
for a in A:
    if gcd(a,X)==1:
        total+=a
        cnt+=1

print(total/cnt)