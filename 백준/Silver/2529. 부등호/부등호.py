import sys
from collections import defaultdict
input=sys.stdin.readline
n=int(input())
arr=list(input().split())
small="99999999999999"
big=""

def makeNum(arr):
    tmp=''
    for i in range(len(arr)):
        tmp+=str(arr[i])
    return tmp

def dfs(L,s):
    global small
    global big
    if L>n-1:
        small=min(small,makeNum(number))
        big=max(big,makeNum(number))
        return
    if arr[L]=='<':
        for i in range(s,10):
            if num[i]==0:
                number.append(i)
                num[i]=1
                dfs(L+1,i)
                number.pop()
                num[i]=0
    elif arr[L]=='>':
        for i in range(s):
            if num[i]==0:
                number.append(i)
                num[i]=1
                dfs(L+1,i)
                number.pop()
                num[i]=0


for i in range(10):
    num=[0]*(10)
    num[i]=1
    number=[i]
    dfs(0,i)
    
print(big)
print(small)
