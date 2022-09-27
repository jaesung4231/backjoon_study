import sys
N=(1000-int(input()))
answer=0
while(N!=0):
    if N>=500:
        answer+=(N//500)
        N=N%500
    elif N>=100:
        answer+=N//100
        N=N%100
    elif N>=50:
        answer+=N//50
        N=N%50
    elif N>=10:
        answer+=N//10
        N=N%10
    elif N>=5:
        answer+=N//5
        N=N%5
    else:
        answer+=N//1
        N=N%1
print(answer)