import sys
import heapq
input=sys.stdin.readline
N=input().strip()
didfind=False
answer=0
def find(N):
    tmp=int(N)
    for n in N:
        tmp+=int(n)
    return tmp

for i in range(int(N)):
    cost=find(str(i))
    if cost==int(N):
        didfind=True
        answer=i
        break

print(answer)
