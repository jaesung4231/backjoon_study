from itertools import permutations, product
import sys
input=sys.stdin.readline
t=int(input())
prime=[0]*1001
prime[0]=1
prime[1]=1
for i in range(4,1001):
    if prime[i]==0:
        isprime=True
        for j in range(2,i):
            if i%j==0:
                isprime=False
                break
        if isprime==False:
            tmp=i
            while tmp<1001:
                prime[tmp]=1
                tmp+=i

for i in range(t):
    num=int(input())
    p=[]
    for i in range(num):
        if prime[i]==0:
            p.append(i)
    found=False
    for j in product(p,repeat=3):
        if sum(j)==num:
            found=True
            break
    ans=sorted(list(j))
    if found==True:
        print(*ans)
    else:
        print(0)

