tmp=[]
num=int(input())
def hanoi(num,A,B):
    if(num==1):
        tmp.append(f'{A} {B}')
        return
    hanoi(num-1,A,6-A-B)
    tmp.append(f'{A} {B}')
    hanoi(num-1,6-A-B,B)

hanoi(num,1,3)
print(len(tmp))
for i in tmp:
    print(i)
