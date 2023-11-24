import sys
from collections import deque

def calculate(a,b,c):
    if c==0:
        if a==0 and b==0:
            return 0
        elif a==1 and b==0:
            return 1
        elif a==0 and b==1:
            return 1
        elif a==1 and b==1:
            return 10
    else:
        if a==0 and b==0:
            return 1
        elif a==1 and b==0:
            return 10
        elif a==0 and b==1:
            return 10
        elif a==1 and b==1:
            return 11

def make(arr):
    tmp=""
    for i in range(len(arr)):
        if arr[i]!="0":
            for j in range(i,len(arr)):
                tmp+=arr[j]
            break
    return tmp[::-1]
T=int(input())

for t in range(T):
    a,b=input().split()
    num1=make(a)
    num2=make(b)
    
    s1=s2=0
    c=0
    ans=""
    MAX=max(len(num1),len(num2))
    tmp=[0]*MAX
    while 1:
        a=b=0
        if s1>=len(num1) and s2>=len(num2):
            break
        if s1<len(num1):
            a=num1[s1]
        if s2<len(num2):
            b=num2[s2]

        cur=calculate(int(a),int(b),c)
        if cur==10:
            c=1
            cur=0
        elif cur==11:
            c=1
            cur=1
        else:
            c=0
            
        s1+=1
        s2+=1
        ans+=str(cur)
    
    if c!=0:
        ans+=str(c)
    
    ans=ans[::-1]
    tmp=""
    if len(ans)>0:
        print(ans)
    else:
        print(0)

    
