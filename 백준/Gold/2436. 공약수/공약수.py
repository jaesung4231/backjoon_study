import sys
import math
input=sys.stdin.readline
a,b=map(int,input().split())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b / gcd(a, b)

ans=1e9
s,e=1,b//a
div=b//a


for i in range(1,(b//a)//2+1):
    if div%i==0:
        c=i
        d=div//i
        if gcd(c,d)!=1:
            continue
        if s+e>c+d:
            s=c
            e=d




print(s*a,e*a)
