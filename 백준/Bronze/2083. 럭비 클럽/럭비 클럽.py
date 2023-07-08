
from itertools import permutations
import sys
input=sys.stdin.readline
while(1):
    a,b,c=input().split()
    age=int(b)
    weight=int(c)
    if a=="#" and b=="0" and c=="0":
        break
    if age>17 or weight>=80:
        print(a,"Senior")
    else:
        print(a,"Junior")
    
    