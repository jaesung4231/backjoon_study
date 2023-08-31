import sys
import math
from collections import deque
input=sys.stdin.readline
S=input().strip()
T=input().strip()
al=len(S)
bl=len(T)

c=math.lcm(al,bl)

al=c//al
bl=c//bl

if S*al==T*bl:
    print(1)
else:
    print(0)