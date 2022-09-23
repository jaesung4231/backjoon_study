from collections import deque
import sys

input=sys.stdin.readline
N=int(input())
for i in range(N):
    p=list(input().strip())
    size=int(input())
    temp=(input().strip())
    arr=[]
    R_count=0
    D_count=0
    if len(temp)!=2:
        arr=list(map(int,temp[1:len(temp)-1].split(',')))
    
    for i in range(len(p)):
        if p[i]=='R':
            R_count+=1
        elif p[i]=='D':
            if len(arr)==0:
                D_count+=1
                break
            if R_count%2==0 or R_count==0:
                arr.pop(0)
            else:
                arr.pop(len(arr)-1)

    
    if D_count==0:
        if (R_count%2)==0 or R_count==0:
            print('[', end="")
            for i in range(len(arr)):
                print(arr[i],end="")
                if i!=len(arr)-1:
                    print(",",end="")
            print(']')
        else:
            arr.reverse()
            print('[', end="")
            for i in range(len(arr)):
                print(arr[i],end="")
                if i!=len(arr)-1:
                    print(",",end="")
            print(']')
    else:
        print("error")