import sys
import heapq
input=sys.stdin.readline
N,K=input().split()
numbers=list(map(int,input().split()))
ans=-1
p=[]

def makenum(p):
    tmp=""
    if len(p)==0:
        return -1
    
    for i in p:
        tmp+=str(i)
    return int(tmp)

def dfs(p):
    global ans
    cost=makenum(p)
    if cost>int(N):
        return
    else:
        ans=max(ans,cost)
    
    for i in range(len(numbers)):
        p.append(numbers[i])
        dfs(p)
        p.pop()

dfs(p)
print(ans)