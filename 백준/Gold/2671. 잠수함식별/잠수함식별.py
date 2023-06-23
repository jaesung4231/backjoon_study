import sys
import math
import re
input=sys.stdin.readline
word=input().strip()
pat=re.compile('(100+1+|01)+')
ans=pat.fullmatch(word)
if ans:
    print("SUBMARINE")
else:
    print("NOISE")