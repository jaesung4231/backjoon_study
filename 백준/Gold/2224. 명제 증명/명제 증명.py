import sys
from itertools import permutations
from collections import defaultdict
input=sys.stdin.readline
n = int(input())
graph=[[0]*58 for _ in range(58)]
cnt=0

for _ in range(n):
    a,b,c=map(str,input().split())
    if a==c: continue
    x=ord(a)-65
    y=ord(c)-65
    if graph[x][y]==0:
        graph[x][y]=1
        cnt+=1
    
for k in range(58):
    for i in range(58):
        for j in range(58):
            if i!=j and not graph[i][j] and graph[i][k] and graph[k][j]:
                graph[i][j]=1
                cnt+=1

print(cnt)
for i in range(58):
    for j in range(58):
        if graph[i][j]:
            print(chr(i+65),"=>",chr(j+65))





    