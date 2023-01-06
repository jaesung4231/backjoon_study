import sys
from collections import deque
input = sys.stdin.readline

n,m=map(int,input().split())

place=[0]*100001
visited=[0]*100001

dx=[-1,1]

def bfs(x):
    place[x]=0
    visited[x]=1
    queue=deque()
    queue.append(x)
    while queue:
        a=queue.popleft()

        if (a*2)<100001 and visited[a*2]==0:
            visited[2*a]=1
            queue.append(2*a)
            place[2*a]=place[a]


        for i in range(2):
            nx=a+dx[i]
            if  0<nx<100000 and visited[nx]==0 :
                queue.append(nx)
                visited[nx]=1
                place[nx]=place[a]+1


        if visited[m]!=0:
            return place[m]

if n>m:
    print(n-m)
else:           
    print(bfs(n))






            




