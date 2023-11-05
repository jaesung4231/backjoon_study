import sys
from collections import deque
input=sys.stdin.readline
N=int(input())
ans=[1e9]*(N+1)
queue=deque()
for i in range(1,N+1):
    if i**2<=N:
        ans[i**2]=1
        queue.append(i**2)

while queue:
    a=queue.popleft()
    for i in range(1,N+1):
        if (a+i**2)<=N:
            if ans[a+i**2]>ans[a]+1:
                ans[a+i**2]=ans[a]+1
                queue.append(a+i**2)
        else:
            break

# print(ans[1:])
print(ans[N])