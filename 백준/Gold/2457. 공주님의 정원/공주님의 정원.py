import sys
input=sys.stdin.readline
N=int(input())
date=[]
answer=[]
for i in range(N):
    tmp=list(map(int,input().split()))
    date.append([(tmp[0]*100)+tmp[1],tmp[2]*100+tmp[3]])

date.sort(key=lambda x:(x[0],x[1]))

answer=[]
result=0
count=0
start=301
end=0
search=0
for i in range(N):
    count=0
    for j in range(search,N):
        if date[j][0]<=start and date[j][1]>end:
            count+=1
            end=date[j][1]
        
        if date[j][0]>start or end>1130:
            search=j
            break
    if count!=0:
        result+=1
        start=end

if end<1201:
    print(0)
else:                
    print(result)
    



        

    



        



        
        


