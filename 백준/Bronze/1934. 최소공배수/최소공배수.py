import sys
num=int(input())
def GCD(x,y):
    while(y):
        x,y=y,x%y    
    return x

def LCM(x,y):
    result=(x*y)//GCD(x,y)
    return result

for i in range(num):
    x,y=map(int,sys.stdin.readline().split())
    print(LCM(x,y))
