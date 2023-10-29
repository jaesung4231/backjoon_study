import sys
from collections import deque
input=sys.stdin.readline
N=int(input())
queue=deque()
for i in range(1,N+1):
    queue.appendleft(i)


while 1:
    if len(queue)==1:
        break
    queue.pop()
    a=queue.pop()
    queue.appendleft(a)

print(queue[0])