import sys
from itertools import combinations
from collections import deque
sys.setrecursionlimit(10**9)
input=sys.stdin.readline
n=int(input())
graph=[[] for _ in range(n+1)]

for _ in range(n-1):
    a,b,c=map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])


def dfs(now,dis,visited):
    global far
    global far_node
    cango=False
    # print(visited,now,dis)
    for i in graph[now]:
        if visited[i[0]]==0:
            cango=True
            visited[i[0]]=1
            dis+=i[1]
            dfs(i[0],dis,visited)
            dis-=i[1]
    if cango==False:
        if dis>far:
            far=dis
            far_node=now
            # print(far,far_node)
    return


visited=[0]*(n+1)
far=-1
far_node=1
visited[1]=1
dfs(1,0,visited)

far=-1
visited=[0]*(n+1)
visited[far_node]=1
dfs(far_node,0,visited)
print(far)

    
    

