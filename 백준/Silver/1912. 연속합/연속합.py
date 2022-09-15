import sys
input=sys.stdin.readline
N=int(input())
data=(list(map(int,input().split())))

def dp(number):
    arr=[]
    tmp=number[0] 
    arr.append(max(number))   
    for i in range(len(number)-1):
        if tmp<0 and number[i+1]>=0:
            arr.append(tmp)
            tmp=number[i+1]

        else:
            # print(tmp, number[i+1])
            if tmp>0 and (tmp+number[i+1])<0:
                arr.append(tmp)
                tmp=0

            elif (number[i+1])<0:
                arr.append(tmp)
                tmp+=number[i+1]

            else:
                tmp+=number[i+1]
    arr.append(tmp)        
    return arr

if len(data)==1:
    print(data[0])
else:
    print(max(dp(data)))