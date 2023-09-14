import sys
import math
from itertools import permutations
input=sys.stdin.readline
N=int(input())
path=input().strip()
print(path.count("EW"))