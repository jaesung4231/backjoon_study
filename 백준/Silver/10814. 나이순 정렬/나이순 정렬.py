from ast import Str
import sys
data=list()
time=0
N=int(input())
for i in range(N):
   a,b = input().split(" ")
   data.append([int(a), b.rstrip(), i])
data=sorted(data, key =lambda x:(x[0], x[2]))
for i in range(N):
    print(int(data[i][0]), data[i][1])