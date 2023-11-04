import sys
from collections import deque
input=sys.stdin.readline

def changetoNum(arr):
    arr=arr.split(":") 
    time=0
    time+=(int(arr[0])*3600)
    time+=(int(arr[1])*60)
    time+=int(arr[2])
    return time

def changetoTime(num):
    hh="0"+str(num//3600)
    num=num%3600
    mm="0"+str(num//60)
    num=num%60
    ss="0"+str(num)
    arr=hh[-2:]+mm[-2:]+ss[-2:]
    if int(arr)%3==0:
        return True
    return False
    




for _ in range(3):
    time=input().split()
    start=time[0]
    end=time[1]
    start=changetoNum(start)
    end=changetoNum(end)
    ans=0
    cur=start
    MAX=(24*3600)
    while cur!=end:
        if changetoTime(cur):
            ans+=1
        cur+=1
        if cur>=MAX:
            cur=0
    if changetoTime(end):
        ans+=1
    print(ans)
