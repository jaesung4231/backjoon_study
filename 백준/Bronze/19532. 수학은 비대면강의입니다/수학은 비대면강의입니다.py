import sys
from collections import deque
a,b,c,d,e,f=map(int,input().split())


x=((c*e)-(f*b))//((a*e)-(d*b))
if b!=0:
    y=(c-a*x)//b
else:
    y=(f-d*x)//e
print(x,y)
