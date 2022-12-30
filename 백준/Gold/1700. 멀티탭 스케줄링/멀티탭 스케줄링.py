import sys
from collections import deque
input=sys.stdin.readline

n, m = map(int, input().split())
numbers= list(map(int, input().split()))
multiTab=[]
ans=0

def check(idx, current):
    t=numbers[idx+1:]
    notuse=False
    tmp=0
    tmp_idx=0
    tmp_2=0
    for i in range(n):
        if multiTab[i] not in t:
            notuse=True
            tmp=multiTab.index(multiTab[i])
            break
        elif multiTab[i] in t and t.index(multiTab[i])>tmp_idx:
            tmp_idx=t.index(multiTab[i])
            tmp_2=multiTab.index(multiTab[i])
    if(notuse):
        multiTab[tmp]=current
    else:
        multiTab[tmp_2]=current
    
    return multiTab

for i in range(m):
    current=numbers[i]
    if len(multiTab)<n and (current not in multiTab):
        multiTab.append(current)
    elif current not in multiTab:
        multiTab=check(i,current)
        ans+=1

print(ans)

    

    
