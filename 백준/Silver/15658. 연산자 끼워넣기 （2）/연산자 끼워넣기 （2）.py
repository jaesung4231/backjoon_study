import sys
from collections import deque
input=sys.stdin.readline
N=int(input())
number=list(map(int,input().split()))
operator=list(map(int,input().split()))
max_ans=-1e9*1e9
min_ans=1e9*1e9

def operate(x,y,o):
    if o==0:
        return x+y
    elif o==1:
        return x-y
    elif o==2:
        return x*y
    else:
        if x<0 and y>0:
            tmp=abs(x)//y
            return tmp*-1
        else:
            return x//y


def calculate(arr):
    cur=number[0]
    if N>2:
        for i in range(1,N):
            cur=operate(cur,number[i],arr[i-1])
    else:
        cur=operate(cur,number[1],arr[0])
    return cur


def dfs(L,p,operator):
    global max_ans
    global min_ans
    if L==N-1:
        cost=calculate(p)
        max_ans=max(max_ans,cost)
        min_ans=min(min_ans,cost)
        return
    for i in range(4):
        if operator[i]==0: continue
        operator[i]-=1
        p.append(i)
        dfs(L+1,p,operator[:])
        p.pop()
        operator[i]+=1

p=[]
dfs(0,p,operator)
print(max_ans)
print(min_ans)
