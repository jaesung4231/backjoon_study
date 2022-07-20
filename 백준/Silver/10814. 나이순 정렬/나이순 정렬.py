import sys
data=list()
N=int(input())
for i in range(N):
   a,b = input().split(" ")
   data.append([int(a), b.rstrip(), i])
data=sorted(data, key =lambda x:(x[0], x[2]))
for i in range(N):
    print(*data[i][:2])