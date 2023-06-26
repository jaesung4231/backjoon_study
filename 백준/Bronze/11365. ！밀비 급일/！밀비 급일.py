import sys
input=sys.stdin.readline
a=input().strip()
while a!="END":
    print(a[::-1])
    a=input().strip()
