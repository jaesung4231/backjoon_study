import sys
N=int(input())
result=[]
data=list(map(int, sys.stdin.readline().split()))
temp=sorted(list(set(data)))
rank={temp[i]: i for i in range(len(temp))}
for i in data:
    print(rank[i], end=' ')
   