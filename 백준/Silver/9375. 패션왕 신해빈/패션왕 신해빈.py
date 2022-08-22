import sys
num=int(input())
dic={}

for _ in range(num):
    sec_num=int(sys.stdin.readline().strip())
    count=0
    temp=1
    for i in range(sec_num):
        name,kind=map(str,sys.stdin.readline().split())
        if kind in dic:
            dic[kind]+=1
        else:
            count+=1
            dic[kind]=1
    result=1
    for i in dic.values():
        result*=(i+1)
    print(result-1)
    dic.clear()

