import sys
input=sys.stdin.readline

n,s=map(int,input().split())
number=list(map(int, input().split()))
ans=0

def dfs(L,sum):
    global ans
    if L>=n:
        return
    sum+=number[L]
    if sum==s:
        ans+=1    
    dfs(L+1,sum-number[L])
    dfs(L+1,sum)

dfs(0,0)
print(ans)
