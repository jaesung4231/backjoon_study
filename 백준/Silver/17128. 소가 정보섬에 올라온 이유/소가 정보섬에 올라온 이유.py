from itertools import permutations
from collections import deque, defaultdict
import sys
input=sys.stdin.readline
N,Q=map(int,input().split())
cow=list(map(int,input().split()))
joke=list(map(int,input().split()))
dp=[0]*N
for i in range(N):
    dp[i]=cow[i]*cow[i-1]*cow[i-2]*cow[i-3]
    
tmp_sum=sum(dp)


for j in joke:
    for i in range(4):
        idx=(j+i-1)%N
        dp[idx]= -dp[idx]
        tmp_sum+=2*dp[idx]
    print(tmp_sum)