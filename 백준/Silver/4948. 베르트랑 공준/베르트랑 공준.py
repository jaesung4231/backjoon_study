import sys

def prime(num):
    arr=[True]*(num+1)
    arr[0]=False
    arr[1]=False

    for i in range(num+1):
        if(arr[i]==True):
            j=2
            while(i*j<=num):
                arr[i*j]=False
                j+=1
    return arr


while(1):
    A=int(input())
    if(A==0):
        break
    arr=prime(A*2)
    result=0
    for i in range(A, len(arr)):
        if(arr[i]==True and i>A):
            result+=1
    print(result)