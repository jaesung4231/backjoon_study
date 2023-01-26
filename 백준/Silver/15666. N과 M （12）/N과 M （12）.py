import sys
input=sys.stdin.readline

n,m=map(int,input().split())
number=sorted(list(map(int,input().split())))
visited=[0]*n
ans=0
p=[]

def dfs(k):
    if len(p)==m:
        print(*p)
    else:
        before=0
        for i in range(k,len(number)):
            if  number[i]!=before:
                p.append(number[i])
                visited[i]=1
                before=number[i]
                dfs(i)
                p.pop()
                visited[i]=0
            
dfs(0)