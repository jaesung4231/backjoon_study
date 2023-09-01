import sys
import heapq
from collections import deque, defaultdict
from queue import PriorityQueue
input=sys.stdin.readline
solved=defaultdict(bool)

N=int(input())
p=[]
p2=[]

for _ in range(N):
    a,b=map(int,input().split())
    heapq.heappush(p,[b,a])
    heapq.heappush(p2,[-b,-a])
    solved[a]=True
M=int(input())

for _ in range(M):
    c=list(map(str,input().split()))
    if c[0] =="add":
        while not solved[-p2[0][1]]:
            heapq.heappop(p2)
        while not solved[p[0][1]]:
            heapq.heappop(p)
        
        heapq.heappush(p,[int(c[2]),int(c[1])])
        heapq.heappush(p2,[-int(c[2]),-int(c[1])])
        solved[int(c[1])]=True
    
    elif c[0] == "solved":
        solved[int(c[1])]=False
    
    else:
        if c[1]=="1":
            while not solved[-p2[0][1]] :
                heapq.heappop(p2)
            print(-p2[0][1])
        else:
            while not solved[p[0][1]]:
                heapq.heappop(p)
            print(p[0][1])