import sys
first_num, sec_num=map(int,sys.stdin.readline().split())

def GCD(x,y):
    while(y):
        x,y=y,x%y    
    return x

def LCM(x,y):
    result=(x*y)//GCD(x,y)
    return result

print(GCD(first_num,sec_num))
print(LCM(first_num,sec_num))