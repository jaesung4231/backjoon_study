from collections import deque, defaultdict
from itertools import combinations, product, permutations
from copy import deepcopy
import sys
input=sys.stdin.readline
n=int(input())
num=[]
two=set()
answer=0

for i in range(n):
    num.append(int(input()))

num.sort()

for i in range(n):
    for j in range(i,n):
        two.add(num[i]+num[j])

for i in range(n-1,-1,-1):
    for j in range(n):
        if num[i]-num[j] in two:
            answer=num[i]
            break            
    if answer!=0:
        break

print(answer)