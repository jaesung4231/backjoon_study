from itertools import permutations
from collections import deque
import sys
input=sys.stdin.readline
n=int(input())
dis=[0]*(n+1)
tree=[[]for _ in range(n+1)]

for _ in range(n-1):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

def bfs(x):
    queue=deque()
    queue.append(x)
    dis[x]=1
    while queue:
        a=queue.popleft()
        for t in tree[a]:
            if dis[t]==0:
                dis[t]=a
                queue.append(t)

bfs(1)
# print(dis)

for i in range(2,n+1):
    print(dis[i])



