import sys
import math
from collections import deque
from itertools import combinations
input=sys.stdin.readline
N=int(input())
if N%2==0:
    ans=[1,2]*(N//2)
    print(*ans)
else:
    ans=[1,2]*(N//2)
    ans.append(3)
    print(*ans)
