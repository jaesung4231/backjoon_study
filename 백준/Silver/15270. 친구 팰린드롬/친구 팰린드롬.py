import sys
from itertools import permutations
input=sys.stdin.readline
n,m=map(int,input().split())
friend=[[] for _ in range(n)]
visited=[0]*(n)

for i in range(m):
    num=list(map(int,input().split()))
    num.sort()
    friend[num[0]-1].append(num[1]-1)


def dfs(L,cnt):
    if L==n: return cnt
    if visited[L]==1: return dfs(L+1,cnt)
    res=0
    for i in range(len(friend[L])):
        if visited[friend[L][i]]==0:
            visited[friend[L][i]]=1
            res=max(res,dfs(L+1,cnt+1))
            visited[friend[L][i]]=0
    return max(res,dfs(L+1,cnt))
    
  
res=dfs(0,0)
res*=2
if res<n:
    print(res+1)
else:
    print(res)

