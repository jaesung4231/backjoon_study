import sys
input=sys.stdin.readline
n,k=map(int,input().split())
ans=0
def gugu(n,k):
    global ans
    for i in range(1,k+1):
        num=str(n*i)
        ans=max(ans,int(num[::-1]))
        

        
gugu(n,k)
print(ans)