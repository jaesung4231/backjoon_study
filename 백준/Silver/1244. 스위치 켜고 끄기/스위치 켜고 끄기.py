import sys
import math
from collections import deque
from itertools import combinations
input=sys.stdin.readline
N=int(input())
switch=[0]+list(map(int,input().split()))

def change(k):
    if switch[k]==1:
        switch[k]=0
    else:
        switch[k]=1

def male(k):
    tmp=k
    while tmp<N+1:
        change(tmp)
        tmp+=k

def female(k):
    left=k-1
    right=k+1
    change(k)
    while 0<left<N+1 and 0<right<N+1:
        if switch[left]==switch[right]:
            change(left)
            change(right)
            left-=1
            right+=1
        else:
            break

def pp():
    tmp=1
    while tmp<N+1:
        print(*switch[tmp:tmp+20])
        tmp+=20

M=int(input())
for _ in range(M):
    a,b=map(int,input().split())
    if a==1:
        male(b)
    else:
        female(b)
pp()
