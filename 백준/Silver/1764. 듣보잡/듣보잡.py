import sys
N,M=map(int,sys.stdin.readline().split())
result=[]
hear=set()
look=set()
for i in range(N):
  hear.add(sys.stdin.readline().strip())
for j in range(M):
  look.add((sys.stdin.readline().strip()))
result = hear.intersection(look)
tt=sorted(result)
tmp=len(result)
print(tmp)
for i in tt:
  print(i)