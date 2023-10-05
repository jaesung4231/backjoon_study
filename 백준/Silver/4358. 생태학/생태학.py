import sys
import math
from collections import deque, defaultdict
from itertools import combinations
input=sys.stdin.readline
trees=defaultdict(int)
pop=defaultdict(float)
total=0
while 1:
    tree=input().strip()
    if tree=="":
        break
    trees[tree]+=1
    total+=1

tree2=sorted(trees.items())

for tree in tree2:
    print("%s %.4f" % (tree[0],(trees[tree[0]]/total)*100))

