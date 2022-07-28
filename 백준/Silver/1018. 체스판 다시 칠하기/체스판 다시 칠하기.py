import sys
N,M=map(int, sys.stdin.readline().split())
arr=[[0 for col in range(M)] for row in range(N)]
opp1=[[0 for col in range(M)] for row in range(N)]
opp2=[[0 for col in range(M)] for row in range(N)]

for i in range(N):
    tmp=input()
    for j in range(len(tmp)):
       arr[i][j]=tmp[j]

def option1(arr):
    for i in range(8):
        for j in range(8):
            if(i%2==0):
                if(j%2==0):
                    arr[i][j]='B'
                else:
                    arr[i][j]='W'
            else:
                if(j%2==0):
                    arr[i][j]='W'
                else:
                    arr[i][j]='B'
    return arr

def option2(arr2):
    for i in range(8):
        for j in range(8):
            if(i%2==0):
                if(j%2==0):
                    arr2[i][j]='W'
                else:
                    arr2[i][j]='B'
            else:
                if(j%2==0):
                    arr2[i][j]='B'
                else:
                    arr2[i][j]='W'
    return arr2

def compare(arr1,arr2):
    num=0
    for i in range(8):
        for j in range(8):
            if arr1[i][j]!=arr2[i][j]:
                num+=1
    return num
m=400000
opp1=option1(opp1)
opp2=option2(opp2)

for j in range((N-7)):
    tmp=[[0 for col in range(8)] for row in range(8)]
    for k in range(M-7):
        for i in range(8):
            tmp[i]=arr[i+j][k:k+8]
        temp=min(compare(tmp,opp1),compare(tmp,opp2))
        if(temp<=m):
            m=temp
           
print(m)

