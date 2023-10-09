import sys
import math
from collections import deque,defaultdict
input=sys.stdin.readline
N,K=map(int,input().split())
S=list(map(int,input().split()))
D=list(map(int,input().split()))
P=[0]*N

def unShuffle():
    for i in range(N):
        P[D[i]-1]=S[i]

for i in range(K):
    unShuffle()
    S=P[:]

print(*P)
