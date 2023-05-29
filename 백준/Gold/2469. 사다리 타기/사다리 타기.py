import sys
input=sys.stdin.readline

def ladder(start, lad):
    for i in range(len(lad)):
        for j in range(k-1):
            if lad[i][j]=='-':
                start[j], start[j+1] = start[j+1], start[j]
                
    return start

k=int(input())
n=int(input())
init=list(range(k))
result=list(input().strip())
for i in range(k):
    result[i]=ord(result[i])-65
lad1=[]
lad2=[]
tmp=True
for i in range(n):
    s=input().strip()
    if '?' in s:
        tmp=False
    elif tmp:
        lad1.append(s)
    else:
        lad2.append(s)
upper=ladder(init, lad1)
lower=ladder(result, lad2[::-1])
i=0
ans=''
while i<k-1:
    if upper[i]==lower[i]:
        ans+='*'
        i+=1
    elif upper[i]==lower[i+1] and upper[i+1]==lower[i]:
        ans+='-'
        i+=1
    elif upper[i]==lower[i-1] and upper[i-1]==lower[i]:
        ans+='*'
        i+=1
    else:
        ans='x'*(k-1)
        break
print(ans)