import sys
data=[]
N=int(input())
for i in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))
data.sort()
for i in range(N):
    print(*data[i])