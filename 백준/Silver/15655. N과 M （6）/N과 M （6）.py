import sys
input=sys.stdin.readline

n,m=map(int,input().split())
number=sorted(list(map(int,input().split())))
ans=0
p=[]

def dfs(L):
    if len(p)==m:
        print(*p)
    else:
        for i in range(L,len(number)):
            if number[i] not in p:
                p.append(number[i])
                dfs(i+1)
                p.pop()
dfs(0)