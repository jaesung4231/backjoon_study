import sys
from collections import deque, defaultdict
input=sys.stdin.readline
L=int(input())
num=list(map(int,input().split()))
N=int(input())
size=max(max(num),N)+1
s=[0]*(size)
a=[]
b=[]
for i in num:
    s[i]=1

if s[N]==1: print(0)
else:
    for i in range(N,size):
        if s[i]!=1:
            a.append(i)
        else: break
            
    for i in range(N-1,0,-1):
        if s[i]!=1:
            b.append(i)
        else: break
    print(len(a)*len(b)+len(a)-1)