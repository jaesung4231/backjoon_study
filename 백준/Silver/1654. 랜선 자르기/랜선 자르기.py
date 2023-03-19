from collections import deque, defaultdict
from itertools import combinations, product, permutations
from copy import deepcopy
import sys
input=sys.stdin.readline
n,m=map(int,(input().split()))
num=[]
for i in range(n):
    num.append(int(input()))
    
mai=max(num)

def check(target):
    total=0
    for i in range(n):
        total+=(num[i]//target)
    return total

def binary_search(target):
    s=1
    e=mai
    while (s<=e):
        mid=(s+e)//2
        if check(mid)>=target:
            s=mid+1
        elif check(mid)<target:
            e=mid-1
    return e

print(binary_search(m))



