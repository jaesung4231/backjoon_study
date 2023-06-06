import sys
from collections import defaultdict, deque
input=sys.stdin.readline
T=int(input())    

def make(test):
    tmp=test[1:len(test)-1].split(',')
    num=deque()
    if tmp:
        for i in range(len(tmp)):
            num.append(int(tmp[i]))
    return num

def out(arr):
    ans="["
    for i in range(len(arr)):
        if i!=0:
            ans+=","
        ans+=str(arr[i])
    ans+="]"
    return ans



for t in range(T):
    order=list(input().strip())
    n=int(input())
    tmp=input().strip()
    R_count=0
    isError=False

    if len(tmp)>2:
        num=make(tmp)
    else:
        num=[]

    for o in order:
        if o=="R":
            R_count+=1
        if o=="D":
            if len(num)==0:
                isError=True
                break
            elif R_count%2!=0:
                num.pop()
            elif R_count%2==0:
                num.popleft()
    
    if isError:
        print("error")
    elif R_count%2!=0:
        num.reverse()
        ans=out(num)
        print(ans)
    else:
        ans=out(num)
        print(ans)



  


