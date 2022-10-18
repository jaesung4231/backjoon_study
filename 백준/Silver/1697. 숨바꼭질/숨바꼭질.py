from collections import deque
import sys
input=sys.stdin.readline
N,K=map(int,input().split())
MAX=10000000
arr=[0]*(MAX)
arr[N]=1
dx=[1,-1]


def bfs(N):
    queue=deque()
    queue.append(N)
    while(queue):
        a=queue.popleft()
        if arr[K]!=0:
            break
        if a<=100000:
            if arr[2*a]==0:
                arr[2*a]=arr[a]+1
                queue.append(2*a)
        for i in range(2):
            nx=a+dx[i]
            if arr[(nx)]==0:
                if nx%2==0 and arr[(nx//2)]!=0:
                    arr[nx]=arr[(nx//2)]+1
                    queue.append(nx)
                else:
                    arr[nx]=arr[a]+1
                    queue.append(nx)


if N<=K:
    bfs(N)
    print(arr[K]-1)
else:
    print(N-K)

