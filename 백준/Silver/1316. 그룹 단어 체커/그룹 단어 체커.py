import sys
num=int(input())
result=0
for i in range(num):
    word=sys.stdin.readline().strip()
    tmp=[]
    for i in word:
        if tmp.count(i)==0 or tmp[len(tmp)-1]==i:
            tmp.append(i)
        else:
            result+=1
            break

print(num-result)