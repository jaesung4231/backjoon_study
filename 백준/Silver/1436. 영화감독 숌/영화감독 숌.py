import sys
N=int(input())
def function(num):
    result=1
    if(num==1):
        return 666
    else:
        num2=667
        while(1):
            count=False
            if '666' in str(num2):
                count=True
            if count:
                result+=1
            if(result==num):
                return num2
            num2+=1
    return num2

print(function(N))