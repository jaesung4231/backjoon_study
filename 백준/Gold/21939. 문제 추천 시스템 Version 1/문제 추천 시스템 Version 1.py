import sys
import heapq
from collections import deque, defaultdict
input=sys.stdin.readline
p1=[]
p2=[]
table=defaultdict(bool)

N=int(input())
for _ in range(N):
    a,b=map(int,input().split())
    heapq.heappush(p1,[b,a])
    heapq.heappush(p2,[-b,-a])
    table[a]=True

M=int(input())

for i in range(M):
    C=list(input().split())
    if C[0]=="add":
        while table[-p2[0][1]]!=True:
            heapq.heappop(p2)
        while table[p1[0][1]]!=True:
            heapq.heappop(p1)     
        
        heapq.heappush(p2,[-int(C[2]),-int(C[1])])
        heapq.heappush(p1,[int(C[2]),int(C[1])])
          
        table[int(C[1])]=True
    
    
    elif C[0]=="solved":
        table[int(C[1])]=False
    else:
        if C[1]=="1":
            while table[-p2[0][1]]!=True:
               heapq.heappop(p2)
            print(-p2[0][1])
        if C[1]=="-1":
            while table[p1[0][1]]!=True:
               heapq.heappop(p1)
            print(p1[0][1])