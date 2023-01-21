import sys
input=sys.stdin.readline

n,m=map(int,input().split())
ans=0

p=[]
def dfs(L):
    if len(p)==m:
        print(' '.join(map(str,p)))
        return
  
    for i in range(L,n+1):
        if i not in p:
            p.append(i)
            dfs(i+1)
            p.pop()

dfs(1)


