import sys
from itertools import permutations
bottle=[[0]*31 for i in range(31)]
for i in range(31):
    bottle[0][i]=1

for i in range(1,31):
    for j in range(1,31):
        if i>j: continue
        bottle[i][j]=bottle[i-1][j]+bottle[i][j-1]
while 1:
    N=int(input())
    if N==0: break
    print(bottle[N][N])