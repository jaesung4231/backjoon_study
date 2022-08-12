def sum(num):
    result=0
    temp=num
    while(num!=0):
        temp1=num%10
        num=num//10
        result+=temp1
    return(result+temp)
answer=set(range(1,10000))
tt=set()
result=set()
for i in range(10000):
    a=i+1
    while(a<10000):
        a=sum(a)
        tt.add(a)
result=sorted(answer-tt)
for i in result:
    print(i)