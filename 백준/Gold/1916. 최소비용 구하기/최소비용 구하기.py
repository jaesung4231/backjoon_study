from collections import deque, defaultdict
from itertools import combinations, product, permutations
from copy import deepcopy
import heapq
import sys
input=sys.stdin.readline
n=int(input())
m=int(input())
graph=[[]*(n+1) for _ in range(n+1)]
distance=[1e9]*(n+1)

for i in range(m):
    a,b,c=map(int,input().split())
    graph[a].append([b,c])
    
def dijskra(k):
    q=[]
    heapq.heappush(q,(0,k))
    distance[k]=0
    while q:
        dis,now=heapq.heappop(q)
        if distance[now]!=dis: continue
        for i in graph[now]:
            cost=i[1]+dis
            if distance[i[0]]>cost:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

s,e=map(int,input().split())
dijskra(s)
print(distance[e])
