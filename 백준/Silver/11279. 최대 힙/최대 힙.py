import sys
import heapq
input=sys.stdin.readline
N=int(input())
num=[]
for _ in range(N):
    x=int(input())
    if x>0:
        heapq.heappush(num,-x)
    else:
        if num:
            print(-1*heapq.heappop(num))
        else:
            print(0)