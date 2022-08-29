from itertools import product
import sys
N,M=map(int,sys.stdin.readline().split())
data=[]
for i in range(1,N+1):
    data.append(i)
for i in product(data,repeat=M):
    print(*i)