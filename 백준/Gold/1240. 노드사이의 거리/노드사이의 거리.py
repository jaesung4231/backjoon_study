import sys
import heapq
from collections import deque
from itertools import combinations
input=sys.stdin.readline
N,M=map(int,input().split())
graph=[[] for _ in range(N+1)]
distance=[[1e9]*(N+1) for _ in range(N+1)]

for i in range(N-1):
    a,b,c=map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
    distance[a][b]=c
    distance[b][a]=c


def pb():
    for i in range(1,N+1):
        for j in range(1,N+1):
            print(distance[i][j], end=" ")
        print()


def bfs(cur,target):
    visit=[0]*(N+1)
    queue=deque()
    queue.append([cur,0])
    visit[cur]=0
    while queue:
        a,b=queue.popleft()
        if a==target:
            return b
        for g in graph[a]:
            if visit[g[0]]==0:
                visit[g[0]]=1
                queue.append([g[0],b+g[1]])
                distance[a][g[0]]=b+g[1]
                distance[g[0]][a]=b+g[1]
         


for j in range(M):
    a,b=map(int,input().split())
    distance[a][a]=0
    distance[b][b]=0
    print(bfs(a,b))



