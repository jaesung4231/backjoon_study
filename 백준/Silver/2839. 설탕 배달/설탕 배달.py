num= int(input())
bag5=0
bag3=0
if(num%5==0):
    result=num//5
else:
    tmp=num-3
    while(tmp>0):
        if(tmp%5==0):
            bag5=tmp//5
            break
        if(tmp<3):
            bag3=-2
            break
        tmp-=3
        bag3+=1
    result=bag3+1+bag5
    
print(result,end='')