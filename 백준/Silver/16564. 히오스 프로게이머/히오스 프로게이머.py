import sys
import heapq
from collections import deque, defaultdict
input=sys.stdin.readline
N,K=map(int,input().split())
level=[]
for i in range(N):
    level.append(int(input()))
level.sort()

middle=False
for i in range(1,N):
    cost=(level[i]-level[i-1])*i
    if K-cost>=0:
        K-=cost
    else:
        print(level[i-1]+(K//i))
        middle=True
        break

if middle==False:
    print(level[N-1]+(K//N))

    