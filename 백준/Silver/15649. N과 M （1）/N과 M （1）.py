import sys
input=sys.stdin.readline

n,m=map(int,input().split())
visited=[0 for _ in range(n+1)]
def dfs(L,n,m,p):
    if L==m :
        for i in p:
            print(i, end=" ")
        print()
    else:
        for i in range(1,n+1):
            if visited[i]==1:
                continue
            p.append(i)
            visited[i]=1
            dfs(L+1,n,m,p)
            p.pop()
            visited[i]=0
                       
dfs(0,n,m,[])