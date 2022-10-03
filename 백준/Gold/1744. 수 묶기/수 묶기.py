import sys
input=sys.stdin.readline
N=int(input())
pos=[]
neg=[]
other=[]
answer=0
for i in range(N):
    num=int(input().strip())
    if num>1:
        pos.append(num)
    elif num<0:
        neg.append(num)
    else:
        other.append(num)
pos.sort()
neg.sort()
other.sort()
pos_len=len(pos)
neg_len=len(neg)
other_len=len(other)

if pos_len>1:
    for i in range(pos_len-1,0,-2):
        answer+=(pos[i]*pos[i-1])
if neg_len>1:
    for i in range(0,neg_len-1,2):
        answer+=(neg[i]*neg[i+1])
if neg_len!=0:
    if  neg_len%2!=0 and 0 not in other:
        other.append(neg[neg_len-1])

if pos_len!=0 and pos_len%2!=0:
    answer+=pos[0]

answer+=sum(other)
    
# print(pos,neg,other)
print(answer,end="")