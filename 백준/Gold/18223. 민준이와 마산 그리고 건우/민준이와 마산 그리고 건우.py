import sys
import heapq
from collections import deque
input=sys.stdin.readline

V,E,P=map(int,input().split())

graph=[[] for _ in range(V+1)]
distance=[9876543210]*(V+1)
distance[0]=0
path=[[] for _ in range(V+1)]
visited=[0]*(V+1)

for i in range(E):
    a,b,c=map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

def dijkstra(k):
    distance[k]=0
    q=[]
    heapq.heappush(q,(0,k))
    while q:
        dis,now=heapq.heappop(q)
        if distance[now]!=dis: continue
        for g in graph[now]:
            cost=dis+g[1]
            if cost<distance[g[0]]:
                distance[g[0]]=cost
                path[g[0]]=[now]
                heapq.heappush(q,(cost,g[0]))
            elif cost==distance[g[0]]:
                distance[g[0]]=cost
                path[g[0]].append(now)
                heapq.heappush(q,(cost,g[0]))

def bfs(k):
    queue=deque()
    queue.append(k)
    while queue:
        a=queue.popleft()
        if a==P:
            return True
        for i in path[a]:
            queue.append(i)
    
    return False

dijkstra(1)

if bfs(V) or P==V or P==1:
    print("SAVE HIM")
else:
    print("GOOD BYE")
