import sys
input=sys.stdin.readline
N=(list(map(int,input().strip())))
N.sort(reverse=True)
if 0 not in N:
    print(-1,end="")
else:
    if sum(N)%3==0:
        ans=''
        for i in N:
            ans+=str(i)
        print(ans,end='')
    else:
        print(-1,end="")
