import sys
S=sys.stdin.readline().strip()
data=[]
for i in range(len(S)):
  start=0
  end=i+1
  while(end<=len(S)):
    data.append(S[start:end])
    end+=1
    start+=1

result=set(data)
print(len(result))
