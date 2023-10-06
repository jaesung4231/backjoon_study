import sys
import math
from collections import deque
from itertools import combinations
input=sys.stdin.readline
N,K=map(int,input().split())

def sigma(n):
    tmp=0
    for i in range(1,n+1):
        tmp+=i
    return tmp

start=sigma(K)
if N<start:
    print(-1)
else:
    k=N-start
    left=k%K
    if left>0:
        print(K)
    else:
        print(K-1)