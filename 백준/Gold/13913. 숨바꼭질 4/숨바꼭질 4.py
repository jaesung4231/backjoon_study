from collections import deque
import sys
input=sys.stdin.readline
n,k=map(int,input().split())
MAX=100001
visited=[[0]*2 for _ in range(MAX)]

dx=[-1,1]

def bfs(n,k):
    queue=deque()
    queue.append(n)
    visited[n][0]=1
    while queue:
        a=queue.popleft()
        if a==k:
            return (visited[k][0]-1)
        for i in (a+1,a-1,2*a):
            nx=i
            if -1<nx<MAX and visited[nx][0]==0: 
                visited[nx][0]=visited[a][0]+1
                visited[nx][1]=a
                queue.append(nx)
    return (visited[k][0]-1)
    

answer=[]
answer.append(k)
print(bfs(n,k))
num=k
while num!=n:
    answer.append(visited[num][1])
    num=visited[num][1]

print(*answer[::-1])







