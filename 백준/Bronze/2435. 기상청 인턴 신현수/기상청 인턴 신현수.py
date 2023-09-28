import sys
import math
from collections import deque
from itertools import combinations
input=sys.stdin.readline
N,K=map(int,input().split())
num=list(map(int,input().split()))
temp=[]
ans=max(num)
for i in range(N-K+1):
    tmp=0
    for j in range(i,i+K):
        tmp+=num[j]
    temp.append(tmp)
print(max(temp))
