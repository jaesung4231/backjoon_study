from collections import deque, defaultdict
from itertools import combinations, product, permutations
from copy import deepcopy
import sys
input=sys.stdin.readline
n=int(input())
num=list(map(int,input().split()))
m=int(input())
targets=list(map(int,input().split()))
num.sort()

def bi(target):
    s=0
    e=n-1
    while (s<=e):
        mid=(s+e)//2
        if num[mid]==target:
            return 1
        elif num[mid]>target:
            e=mid-1
        elif num[mid]<target:
            s=mid+1
    return 0

for t in targets:
    print(bi(t))
   

