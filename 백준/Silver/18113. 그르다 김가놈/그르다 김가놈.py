import sys
input=sys.stdin.readline
n,k,m=map(int,input().split())
kimbab=[]
ans=-1

for i in range(n):
    l=int(input())
    if l>2*k:
        kimbab.append(l-2*k)
    elif l<2*k and l>k:
        kimbab.append(l-k)

def cut(p):
    cuts=0
    for k in kimbab:
        cuts+=k//p
    return cuts

def b_search():
    global ans
    left=1
    right=max(kimbab)
    while left<=right:
        mid=(left+right)//2
        cur=cut(mid)
        if cur>=m:
            left=mid+1
            ans=max(ans,mid)
        elif cur<m:
            right=mid-1

if kimbab:
    b_search()
print(ans)