from itertools import combinations, permutations
import sys
N,M=map(int,sys.stdin.readline().split())
data=[]
for i in range(1,N+1):
    data.append(i)
result=sorted(combinations(data,M))
for i in result:
    print(*i)