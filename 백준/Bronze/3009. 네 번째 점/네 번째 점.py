import sys
x1,y1=map(int, sys.stdin.readline().split())
x2,y2=map(int, sys.stdin.readline().split())
x3,y3=map(int, sys.stdin.readline().split())

if(x1==x2):
    x=x3
    if(y1==y3):
        y=y2
    else:
        y=y1
elif(x1==x3):
    x=x2
    if(y1==y2):
        y=y3
    else:
        y=y1
else:
    x=x1
    if(y2==y1):
        y=y3
    else: 
        y=y2

print(x,y)