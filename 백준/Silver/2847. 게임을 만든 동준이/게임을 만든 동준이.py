import sys
input=sys.stdin.readline
N=int(input())
number=[]
answer=0
for i in range(N):
    number.append(int(input().strip()))
for i in range(N-1,0,-1):
    if number[i-1]>=number[i]:
        answer+=(number[i-1]-number[i]+1)
        number[i-1]=(number[i]-1)

print(answer)