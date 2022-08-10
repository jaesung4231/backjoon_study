import sys
N,k =map(int, sys.stdin.readline().split())
data=list(map(int, sys.stdin.readline().split()))
data.sort()
print(data[N-k])