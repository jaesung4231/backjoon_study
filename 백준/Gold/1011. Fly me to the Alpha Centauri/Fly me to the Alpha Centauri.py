from collections import deque, defaultdict
from itertools import combinations, product, permutations
from copy import deepcopy
import heapq
import sys
input=sys.stdin.readline
T=int(input())
for _ in range(T):
    x, y = map(int,input().split())
    distance = y - x
    count = 0 
    move = 1  
    move_plus = 0  
    while move_plus < distance :
        count += 1
        move_plus += move
        if count % 2 == 0 : 
            move += 1  
    print(count)