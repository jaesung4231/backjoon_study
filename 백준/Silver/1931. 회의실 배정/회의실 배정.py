import sys
N=int(input())
time=[[0]*2 for _ in range(N)]

for i in range(N):
    start,end=map(int, sys.stdin.readline().split())
    time[i][0]=start
    time[i][1]=end

time.sort(key=lambda x:(x[1],x[0]))
end_time=time[0][1]
result=1
for i in range(1,len(time)):
    if end_time<=time[i][0]:
        result+=1
        end_time=time[i][1]
    
print(result)