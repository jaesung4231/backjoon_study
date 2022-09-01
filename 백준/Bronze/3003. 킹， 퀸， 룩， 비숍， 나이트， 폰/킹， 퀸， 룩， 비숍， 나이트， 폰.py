import sys
data=[1,1,2,2,2,8]
input=list(map(int,sys.stdin.readline().split()))
for i in range(6):
    data[i]=data[i]-input[i]
print(*data)