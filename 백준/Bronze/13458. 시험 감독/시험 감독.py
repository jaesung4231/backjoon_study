from collections import deque
import copy
import sys
input=sys.stdin.readline
N=int(input())
room=list(map(int,input().split()))
B,C=(map(int,input().split()))
for i in range(N):
    room[i]=room[i]-B

per=0
for i in range(N):
    if room[i]>C:
        if room[i]%C!=0:
            per+=(room[i]//C)+1
        else:
            per+=(room[i]//C)
    elif room[i]>0:
        per+=1
print(per+N)
