import sys
import math
import heapq
from collections import defaultdict, deque
input=sys.stdin.readline
N=int(input())
for _ in range(N):
    a,b=map(int,input().split())
    print(math.lcm(a,b))
