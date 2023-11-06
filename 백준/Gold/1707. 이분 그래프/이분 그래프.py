import sys
from collections import deque
input=sys.stdin.readline



def bfs(x):
    queue=deque()
    queue.append(x)
    visited[x]=1
    while queue:
        a=queue.popleft()
        for g in graph[a]:
            if visited[g]==0:
                visited[g]=1
                color[g] = not color[a]
                queue.append(g)
            else:
                if color[g]==color[a]:
                    return False
    return True


K=int(input())
for _ in range(K):
    V,E=map(int,input().split())
    graph=[[] for _ in range(V+1)]
    color=[False]*(V+1)
    visited=[0]*(V+1)
    for _ in range(E):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    isBipartite=True
    for i in range(1,V+1):
        if len(graph[i])>0:
            if bfs(i)==False:
                isBipartite=False
                break

    if isBipartite:
        print("YES")
    else:
        print("NO")
