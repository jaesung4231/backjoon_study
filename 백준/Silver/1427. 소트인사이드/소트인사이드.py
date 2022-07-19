N=input()
num=[]
for i in N:
    num.append(int(i))
num.sort()
num.reverse()
result=""
for i in num:
    result=result+str(i)
print(int(result))