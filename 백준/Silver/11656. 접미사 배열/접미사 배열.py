import sys
import heapq
from collections import deque
from itertools import combinations
input=sys.stdin.readline
sub=[]
word=input().strip()
for i in range(len(word)):
    sub.append(word[i:])
sub.sort()
for s in sub:
    print(s)