import sys
data=[]
N=int(input())
for i in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))

data.sort(key=lambda x: x[0])
data.sort(key=lambda x: x[1])
for i in range(N):
    print(*data[i])