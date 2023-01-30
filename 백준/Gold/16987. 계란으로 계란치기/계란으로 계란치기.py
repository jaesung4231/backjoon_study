from collections import deque, defaultdict
from copy import deepcopy
from itertools import permutations, combinations
import sys
input=sys.stdin.readline

eggs=[]
p=[]
t=int(input())
cnt=0

for i in range(t):
    eggs.append(list(map(int,input().split())))

def dfs(L):
    global cnt
    Allbreak=True
    if L==t:
        count=0
        for i in range(t):
            if eggs[i][0]<=0:
                count+=1
        cnt=max(cnt,count)
        return
    else:
        now=eggs[L]
    

    if now[0]<=0:
        dfs(L+1)
        return
 
    for i in range(t):
        if i==L:
            continue
        if eggs[i][0]>0:
            Allbreak=False
            break


    if Allbreak:
        cnt=max(cnt,t-1)
        return

    for i in range(t):
        if i==L:
            continue
        if eggs[i][0]<=0:
            continue
        eggs[i][0]-=now[1]
        now[0]-=eggs[i][1]
        dfs(L+1)
        eggs[i][0]+=now[1]
        now[0]+=eggs[i][1]


dfs(0)
print(cnt)

