import sys
x,y,w,h=map(int,sys.stdin.readline().split())
num1=min((w-x),x)
num2=min((h-y),y)
result=min(num1, num2)
print(result)