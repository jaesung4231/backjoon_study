import sys
temp=[0]*20000000
num=int(input())
data=list(map(int, sys.stdin.readline().split()))
for i in range(len(data)):
  temp[data[i]]+=1
num_2=int(input())
input_data=list(map(int,sys.stdin.readline().split()))
for i in input_data:
  print(temp[i], end=' ')

