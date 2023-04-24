from collections import deque, defaultdict
from itertools import combinations, product, permutations
from queue import PriorityQueue
from copy import deepcopy
import sys
import heapq
input=sys.stdin.readline
v,e=map(int,input().split())
k=int(input())
pq=[]
graph=[[]*(v+1) for _ in range(v+1)]
distance=[1e9]*(v+1)

for i in range(e):
    a,b,c=map(int,input().split())
    graph[a].append([b,c])

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0

    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(k)

for i in range(1,v+1):
    if distance[i]==1e9:
        print("INF")
    else:
        print(distance[i])
