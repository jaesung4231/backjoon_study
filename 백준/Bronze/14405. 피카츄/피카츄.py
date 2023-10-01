import sys
import math
from collections import deque
from itertools import combinations
input=sys.stdin.readline
word=input().strip()
isShort=False
if len(word)==0:
    isShort=True
def check(arr):
    for a in arr:
        if a!='*':
            return False
    return True

word=word.replace('pi',"*")
word=word.replace('ka',"*")
word=word.replace('chu',"*")

if check(word) and len(word)!=0:
    print("YES")
else:
    print("NO")