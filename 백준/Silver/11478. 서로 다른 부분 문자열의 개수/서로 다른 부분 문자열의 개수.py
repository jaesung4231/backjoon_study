import sys
from itertools import permutations
input=sys.stdin.readline
word=set()
S=input().strip()
word.add(S)

for s in S:
    word.add(s)

for i in range(1,len(S)):
    s=0
    while s+i<len(S)+1:
        word.add(S[s:s+i])
        s+=1

print(len(word))
