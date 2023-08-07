import sys
from collections import deque
input=sys.stdin.readline
T=int(input())
for _ in range(T):
    cnt=0
    n,m=map(int,input().split())
    for i in range(n,m+1):
        num=str(i)
        cnt+=num.count('0')
    print(cnt)