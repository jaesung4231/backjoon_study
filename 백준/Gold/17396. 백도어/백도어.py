from collections import deque, defaultdict
from itertools import combinations, product, permutations
from copy import deepcopy
import heapq
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
point=list(map(int,input().split()))
point[n-1]=0
graph=[[] for _ in range(n)]
distance=[100000*100000+1]*(n)

for _ in range(m):
    a,b,t=map(int,input().split())
    if point[a]!=1 and point[b]!=1:
        graph[a].append([b,t])
        graph[b].append([a,t])

def dijkstra(k):
    distance[k]=0
    q=[]
    heapq.heappush(q,(0,k))
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]!=dist: continue
        for i in graph[now]:
            cost=i[1]+dist
            if distance[i[0]]>cost:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(0)
if distance[n-1]!=100000*100000+1:
    print(distance[n-1])
else:
    print(-1)