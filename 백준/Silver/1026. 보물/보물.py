import sys
input=sys.stdin.readline
N=int(input())
A=sorted(list(map(int,input().split())))
B=sorted(list(map(int,input().split())))
answer=0
for i in range(N):
    answer+=A[N-i-1]*B[i]
print(answer)
