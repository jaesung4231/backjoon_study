from collections import deque, defaultdict
from itertools import permutations, combinations
import sys
input=sys.stdin.readline
number=[-1]

def dfs(k):
    if len(p)==6:
        for i in p:
            print(i, end=" ")
        print()
    else:
        before=0
        for i in range(k,len(number)):
            if number[i]!=before:
                p.append(number[i])
                visited[i]=1
                before=number[i]
                dfs(i+1)
                p.pop()
        
while 1:
    number=list(map(int,input().split()))
    if number[0]==0:
        break
    else:
        visited=[0]*(len(number))
        m=number[0]
        p=[]
        dfs(1)
        print()