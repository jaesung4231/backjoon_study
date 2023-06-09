import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
for i in range(n):
    stack=[]
    arr=input().strip()
    for a in arr:
        V=True
        if a=="(":
            stack.append("(")
        else:
            if len(stack)>0:
                stack.pop()
            else:
                V=False
                break
    if stack or V==False:
        print("NO")
    else:
        print("YES")


