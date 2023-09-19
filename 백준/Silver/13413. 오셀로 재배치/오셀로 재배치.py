import sys
import math
from collections import deque
input=sys.stdin.readline
T=int(input())
for t in range(T):
    N=int(input())
    visit=[0]*N
    cell=input().strip()
    target=input().strip()
    cnt=0
    for i in range(N):
        if cell[i]!=target[i] and visit[i]==0:
            switch=False
            for j in range(i+1,N):
                if cell[j]!=target[j] and cell[i]==target[j] and visit[j]==0:
                    cnt+=1
                    visit[j]=1
                    switch=True
                    break
            if switch==False:
                cnt+=1        
        visit[i]=1
    print(cnt)
            