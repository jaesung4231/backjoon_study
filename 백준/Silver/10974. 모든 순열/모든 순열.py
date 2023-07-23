import sys
from itertools import permutations
input=sys.stdin.readline
n=int(input())
for p in permutations(range(1,n+1),n):
    print(*p)