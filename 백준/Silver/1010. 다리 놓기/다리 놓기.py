import sys
def factorial(x):
    result=1
    for i in range(1,x+1):
        result*=i
    return result

num=int(input())
for _ in range(num):
    n,k=map(int,sys.stdin.readline().split())
    print(factorial(k)//(factorial(n)*factorial(k-n)))
