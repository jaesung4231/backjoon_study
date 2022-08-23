import sys
num=int(input())
time=list(map(int,sys.stdin.readline().split()))
time.sort()
tmp=0
result=0
for i in time:
    tmp+=i
    result+=tmp
print(result)