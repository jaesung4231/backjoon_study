from collections import deque, defaultdict
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
number=[]
for i in range(n):
    number.append(int(input()))
number.sort()
# print(number)
left=0
right=0
answer=2000000000

while left!=n-1:
    S=number[right]-number[left]
    if S==m:
        answer=S
        break
    if S<answer and m<=S:
        answer=S
    if S<m and right<n-1:
        right+=1
    else:
        left+=1

print(answer)



    



