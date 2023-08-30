import sys
from collections import defaultdict
input=sys.stdin.readline
didCome=defaultdict(int)
didLeft=defaultdict(int)
ans=0
def make_Time(time):
    h,m = time.split(':')
    t=int(h)*60+int(m)
    return t

S,M,E=map(str,input().split())
S,M,E=make_Time(S),make_Time(M),make_Time(E)

def check(time,name):
    global ans
    if time<=S:
        didCome[name]+=1
    
    if name in didCome and M<=time<=E:
        didLeft[name]+=1

while 1:
    try:
        time,name=input().split()
        check(make_Time(time),name)
    except:
        print(len(didLeft))
        break



