import sys
real_num=int(input())
data=list(map(int, sys.stdin.readline().split()))
data.sort()
print(data[0]*data[len(data)-1])