import sys
from collections import deque
input=sys.stdin.readline
num=list(map(int,input().split()))
num.sort()
print(*num)