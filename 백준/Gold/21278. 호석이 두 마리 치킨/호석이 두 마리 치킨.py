import sys
from collections import deque
from itertools import combinations
input=sys.stdin.readline
n,m=map(int,input().split())
graph=[[] for _ in range(n)]
dis_ans=1e9

for i in range(m):
    a,b=map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

def bfs(x,y,visited):
    queue=deque()
    queue.append(x)
    queue.append(y)
    total=0
    while queue:
        a=queue.popleft()
        for g in graph[a]:
            if g==x or g==y:
                continue
            if visited[g]==0:
                queue.append(g)
                visited[g]=visited[a]+1
                total+=visited[g]
    # print(total,visited)
    return total


for com in combinations((range(0,n)),2):
    a,b=com[0],com[1]
    visited=[0]*n
    dis=bfs(a,b,visited)
    cost=dis
    if cost<dis_ans:
        dis_ans=cost
        answer=sorted(com)
    
print(answer[0]+1,answer[1]+1,dis_ans*2)

