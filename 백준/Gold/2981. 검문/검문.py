import sys
def GCD(x,y):
    while(y):
        x,y=y,x%y
    return x

def LCM(x,y):
    return x*y/GCD(x,y)

def CD(x):
    result=[]
    for i in range(2, int(x**(1/2))+1):
        if x%i==0:
            result.append(i)
            result.append(x//i)
    result.append(x)
    result=list(set(result))
    result.sort()
    return result

data=[]
data_2=[]
data_3=[]

num=int(input())
for i in range(num):
    data.append(int(sys.stdin.readline().strip()))
data.sort()

for i in range(1,num):
    data_2.append(data[i]-data[i-1])
data_2.sort()

prev=data_2[0]
for i in range(1,len(data_2)):
    prev = GCD(prev, data_2[i])

data_3=CD(prev)

for i in data_3:
    print(i, end=" ")

