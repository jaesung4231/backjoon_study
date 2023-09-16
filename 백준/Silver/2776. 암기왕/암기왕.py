import sys
import math
from itertools import permutations
input=sys.stdin.readline
T=int(input())



def binary_search(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        cost=arr[mid]
        if cost==target:
            return 1
        elif cost>target:
            right=mid-1
        elif cost<target:
            left=mid+1
    return 0



for t in range(T):
    n=int(input())
    num=sorted(list(map(int,input().split())))
    m=int(input())
    mum=(list(map(int,input().split())))
    tmp=sorted(num)
    table={}
    for m in mum:
        table[m]=(binary_search(tmp,m))

    for m in mum:
        print(table[m])
