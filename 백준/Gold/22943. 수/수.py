import sys
import heapq
from collections import deque
from itertools import permutations
input=sys.stdin.readline

K,M=map(int,input().split())
MAX=10**(K)
prime=[0]*MAX
added=[0]*MAX
multi=[0]*MAX

prime[0]=1
prime[1]=1


for i in range(MAX):
    if prime[i]==0:
        t=i+i
        while t<MAX:
            prime[t]=1
            t+=i

for i in range(MAX):
    if not prime[i]:
        for j in range(i+1):
            if not prime[j]:
                if (i+j)<MAX and i!=j:
                    added[i+j]=1
                if (i*j)<MAX:
                    multi[i*j]=1

def divide(s):
    while s%M==0:
        s=(s//M)
    return s

def makenum(arr):
    tmp=''
    for a in arr:
        tmp+=str(a)
    return int(tmp)

ans=0

for p in permutations(range(10),K):
    num=list(p)
    if num[0]==0: continue
    n=makenum(num)
    if multi[divide(n)]==1 and added[n]==1:
        ans+=1
print(ans)
    

# for i in range(1,MAX):
#     if multi[divide(i)]==1 and added[i]==1:
#         ans+=1
# print(ans)
