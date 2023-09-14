import sys
import math
from collections import deque
from itertools import permutations, combinations
input=sys.stdin.readline
N=int(input())
P=list(map(int,input().split()))
M=int(input())

num=[]
for i in range(N):
    num.append([i,P[i]])
num.sort(key=lambda x: [x[1],-x[0]])

tmp=[num[0][0]]*(M//num[0][1])
cost=num[0][1]*(M//num[0][1])

didchange=False
for i in range(len(tmp)):
    for j in range(N-1,-1,-1):
        if j>tmp[i]:
            if cost-P[tmp[i]]+P[j]<=M:
                cost=cost-P[tmp[i]]+P[j]
                didchange=True
                tmp[i]=j
        else:
            break
    if didchange==False and tmp[i]==0:
        cost-=P[tmp[i]]


answer=""
for i in range(len(tmp)):
    answer+=str(tmp[i])
print(int(answer))
