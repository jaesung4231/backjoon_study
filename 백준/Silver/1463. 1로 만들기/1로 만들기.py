import sys
N=int(input())
num=[0]*(N+1)
for i in range(2,N+1):
  num[i]=num[i-1]+1
  if i%2==0:
    num[i]=min(num[i],num[i//2]+1)
  if i %3==0:
    num[i]=min(num[i],num[i//3]+1)

print(num[N])