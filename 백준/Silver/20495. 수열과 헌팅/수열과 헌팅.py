import sys
import bisect
input=sys.stdin.readline
n=int(input())
up=[]
low=[]
visit=[[] for _ in range(n)]


for i in range(n):
    a,b=map(int,input().split())
    low.append(a-b)
    up.append(a+b)

loworder=low[:]
bigorder=up[:]

low.sort()
up.sort()

for i in range(n):
    print(bisect.bisect_left(up,loworder[i])+1,bisect.bisect_right(low,bigorder[i]))





