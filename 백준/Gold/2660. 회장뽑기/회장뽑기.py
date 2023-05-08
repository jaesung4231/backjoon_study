from collections import deque, defaultdict
from itertools import combinations, product, permutations
from queue import PriorityQueue
from copy import deepcopy
import sys
import heapq
n=int(input())
graph=[[] for _ in range(n+1)]
board=[]

for i in range(n+1):
    board.append([1e9]*(n+1))

while(1):
    a,b=map(int,input().split())
    if a==-1 and b==-1:
        break
    graph[a].append(b)
    graph[b].append(a)

def bfs(k,dis):
    queue=deque()
    visited=[0]*(n+1)
    queue.append(k)
    visited[k]=1
    while queue:
        a=queue.popleft()
        for i in graph[a]:
            if visited[i]==0:
                visited[i]=visited[a]+1
                queue.append(i)
                dis=max(dis,visited[i])
    return dis

ans=[0]*(n+1)
for i in range(1,n+1):
    ans[i]=bfs(i,0)-1

k=min(ans[1:])
print(k,ans.count(k))
l=[]
for i in range(1,n+1):
    if ans[i]==k:
        print(i, end=" ")
