import sys
def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fibo(n):
    f=[0,1]
    count=0
    if n>=2:
        for i in range(2,n+1):
            count+=1
            f.append(f[i-1]+f[i-2])
    return count-1

N=int(input())
fib(N)
fibo(N)
print(fib(N), fibo(N), end="")