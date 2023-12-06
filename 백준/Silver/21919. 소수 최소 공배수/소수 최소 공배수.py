import sys
import math
from collections import deque
N=int(input())
num = list(map(int,input().split()))
prime=[0]*1000001
prime[0]=1
prime[1]=1
for i in range(len(prime)):
    if prime[i]==0:
        tmp=i*2
        while tmp<len(prime):
            prime[tmp]=1
            tmp+=i

tmp =[]
for number in num:
    if prime[number]==0:
        tmp.append(number)

if len(tmp)==0:
    print(-1)
elif len(tmp)==1:
    print(tmp[0])
else:
    ans=tmp[0]
    for i in range(1,len(tmp)):
        ans=math.lcm(ans,tmp[i])
    print(ans)
    