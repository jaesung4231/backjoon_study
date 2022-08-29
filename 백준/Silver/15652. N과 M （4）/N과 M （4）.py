from itertools import combinations_with_replacement, product
import sys
N,M=map(int,sys.stdin.readline().split())
data=[]
for i in range(1,N+1):
    data.append(i)

for i in combinations_with_replacement(data, M):
    print(*i)