import sys
data=[]
N=int(input())
for i in range(N):
    data.append(input())

result=list(set(data))
result.sort()
result.sort(key=lambda x: len(x))

for i in range(len(result)):
    print(result[i])
