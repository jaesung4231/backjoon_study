import sys
from collections import defaultdict
from itertools import permutations
input=sys.stdin.readline
n=int(input())
m=int(input())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

plan=list(map(int,input().split()))

for i in range(n):
    for j in range(n):
        if graph[i][j]==0:
            graph[i][j]=1e9

for i in range(n):
    graph[i][i]=0

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

cantgo=False
for i in range(len(plan)-1):
    if graph[plan[i]-1][plan[i+1]-1]>=1e9:
        cantgo=True
        break

if cantgo==True:
    print("NO")
else:
    print("YES")
