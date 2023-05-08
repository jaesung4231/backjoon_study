import sys
input=sys.stdin.readline
n=int(input())
A=0
B=0
A_ans=0
B_ans=0
before=0
FULLTIME=48*60
for i in range(n):
    team,time=input().split()
    h,m=time.split(':')
    scoretime=int(h)*60+int(m)
    if A>B:
        A_ans+=(scoretime-before)
    elif B>A:
        B_ans+=(scoretime-before)
    before=scoretime
    if int(team)==1:
        A+=1
    elif int(team)==2:
        B+=1    


if A>B:
    A_ans+=(FULLTIME-before)
elif B>A:
    B_ans+=(FULLTIME-before)

A_h=str(A_ans//60)
A_m=str(A_ans%60)
B_h=str(B_ans//60)
B_m=str(B_ans%60)
if len(A_h)==1:
    A_h='0'+A_h
if len(A_m)==1:
    A_m='0'+A_m
if len(B_h)==1:
    B_h='0'+B_h
if len(B_m)==1:
    B_m='0'+B_m
print(A_h+":"+A_m)
print(B_h+":"+B_m)



    