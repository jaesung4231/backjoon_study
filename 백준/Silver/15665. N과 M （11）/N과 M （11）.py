from collections import deque, defaultdict
from itertools import permutations, combinations
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
        for i in range(len(number)):
            if  number[i]!=before:
                p.append(number[i])
                visited[i]=1
                before=number[i]
                dfs(i+1)
                p.pop()
                visited[i]=0
dfs(0)