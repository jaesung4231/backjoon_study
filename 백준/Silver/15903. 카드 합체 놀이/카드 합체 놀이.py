from collections import deque
from copy import deepcopy
import sys
input=sys.stdin.readline
N,M=map(int,input().split())
num=list(map(int,input().split()))
for i in range(M):
    num.sort()
    tmp=num[0]+num[1]
    num[0]=tmp
    num[1]=tmp
print(sum(num))