import sys

def GCD(x,y):
    while(y):
        x,y=y,x%y
    return x
def LCM(x,y):
    return x*y/GCD(x,y)

num=int(input())
data=list(map(int,sys.stdin.readline().split()))
first=data[0]
for i in range(1,len(data)):
    temp=GCD(first,data[i])
    print(str(first//temp) +'/' + str(data[i]//temp))

 