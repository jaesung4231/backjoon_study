import sys
N,M=map(int,sys.stdin.readline().split())
data=list(map(int,sys.stdin.readline().split()))
for i in range(N-1):
    data[i+1]+=data[i]
data=[0]+data
for i in range(M):
    s,e=map(int,sys.stdin.readline().split())
    print(data[e]-data[s-1])

    