import sys
input=sys.stdin.readline
N,M=map(int,input().split())
B=[]
for i in range(N):
    n=int(input())
    B.append(n)    
B.sort()

def b_search(k):
    left=0
    right=N-1
    ans=-1
    while left<=right:
        mid=(left+right)//2
        cost=B[mid]
        if cost>=k:
            if cost==k:
                ans=mid
            right=mid-1
        else:
            left=mid+1    
    return ans

for i in range(M):
    a=int(input())
    print(b_search(a))
