import sys
N=int(input())
s = [0 for i in range(301)]
result = [0 for i in range(301)]
for i in range(N):
    s[i]=(int(sys.stdin.readline()))

result[0]=s[0]
result[1]=max(s[0]+s[1],s[1])
result[2]=max(s[1]+s[2],s[0]+s[2])

for i in range(3,N):
    result[i]=max(result[i-3]+s[i-1]+s[i],result[i-2]+s[i])

print(result[N-1],end="")