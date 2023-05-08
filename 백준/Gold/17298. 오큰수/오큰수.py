import sys
input=sys.stdin.readline
n=int(input())
num=list(map(int,input().split()))
answer = [-1] * n
stack = []
stack.append(0)
for i in range(1, n):
    while stack and num[stack[-1]] < num[i]:
        answer[stack.pop()] = num[i]
   
    stack.append(i)


print(*answer)