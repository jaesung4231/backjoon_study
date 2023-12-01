import sys
from collections import deque
A,B=map(int,input().split())
table=['4','7']
cnt=0
def makeNumber(arr):
    if len(arr)==0:
        return 0
    tmp=""
    for a in arr:
        tmp+=a
    return int(tmp)

def search(arr):
    global cnt
    cost=makeNumber(arr)
    # print(cost)
    if cost>B:
        return
    elif cost>=A:
        cnt+=1

    for i in range(2):
        arr.append(table[i])
        search(arr)
        arr.pop()

p=[]
search(p)
print(cnt)
