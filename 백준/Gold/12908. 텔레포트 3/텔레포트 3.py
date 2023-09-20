import sys
import heapq
from collections import deque, defaultdict
input=sys.stdin.readline
MAX=1e9*2+1
def distance(d1,d2):
    return abs(abs(d1[0]-d2[0])+abs(d1[1]-d2[1]))
dot=[]
xs,ys=map(int,input().split())
xe,ye=map(int,input().split())
dot.append([xs,ys])
dot.append([xe,ye])
table=defaultdict(list)
graph=[[MAX]*8 for _ in range(8)]

for i in range(3):
    a,b,c,d=map(int,input().split())
    dot.append([a,b])
    dot.append([c,d])

for i in range(8):
    graph[i][i]=0
    for j in range(8):
        if i>0 and i%2==0 and j==i+1:
            graph[i][j]=min(graph[i][j],10,distance(dot[i],dot[j]))
            graph[j][i]=min(graph[i][j],10,distance(dot[i],dot[j]))
        else:
            graph[i][j]=min(graph[i][j],distance(dot[i],dot[j]))


for k in range(8):
    for i in range(8):
        for j in range(8):
            if graph[i][j]>=graph[i][k]+graph[k][j]:
                graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

print(graph[0][1])