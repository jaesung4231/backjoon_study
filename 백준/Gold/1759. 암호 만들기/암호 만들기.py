from collections import deque, defaultdict
from itertools import permutations, combinations
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
arr=sorted(list(input().split()))
visited=[0]*m
p=[]
table={'a','e','i','o','u'}
def dfs(k):
    if len(p)==n:
        ans=""
        cnt=0
        cnt2=0
        for i in p:
            if i in table:
                cnt+=1
            else:
                cnt2+=1
            ans+=i
        if cnt>=1 and cnt2>=2:
            print(ans)
    else:
        before='a'
        for i in range(k,len(arr)):
            if arr[i]>=before and visited[i]==0:
                p.append(arr[i])
                before=arr[i]
                visited[i]=1
                dfs(i+1)
                p.pop()
                visited[i]=0

dfs(0)


