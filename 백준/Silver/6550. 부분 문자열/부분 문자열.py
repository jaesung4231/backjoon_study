import sys
from collections import deque
input=sys.stdin.readline

while 1:
    try:
        S,T=input().split()
        cur=0
        visit=[0]*len(S)
        for t in T:
            if t==S[cur]:
                visit[cur]=1
                if cur<len(S)-1:
                    cur+=1
        isSub=True
        for v in visit:
            if v==0:
                isSub=False
                break
        if isSub:
            print("Yes")
        else:
            print("No")

    except:
        break