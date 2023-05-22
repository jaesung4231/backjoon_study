from itertools import combinations
from collections import deque
import math
import sys
input=sys.stdin.readline
n=int(input())
m=int(input())
sensor=list(set(map(int,input().split())))
sensor.sort()
diff=[]
for i in range(1,len(sensor)):
    diff.append(sensor[i]-sensor[i-1])
diff.sort()

for i in range(m-1):
    if diff:
        diff.pop()
    else:
        break
print(sum(diff))
