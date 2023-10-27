import sys
import heapq
input=sys.stdin.readline
N=int(input())
trophy=[]

for _ in range(N):
    trophy.append(int(input()))


canSee=[1]*N
for i in range(N):
    for j in range(i+1,N):
        if trophy[j]<=trophy[i]:
            canSee[j]=0

print(canSee.count(1))          
trophy.reverse()

canSee=[1]*N
for i in range(N):
    for j in range(i+1,N):
        if trophy[j]<=trophy[i]:
            canSee[j]=0
print(canSee.count(1))