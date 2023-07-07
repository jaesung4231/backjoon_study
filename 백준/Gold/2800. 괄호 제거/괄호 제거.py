import sys
from itertools import combinations
input=sys.stdin.readline
sentence=input().strip()
stack=[]
bracket=[]
ans=set()

L=len(sentence)
for s in range(L):
    if sentence[s]=="(":
        stack.append(s)
    elif sentence[s]==")":
        bracket.append([stack.pop(),s])

# print(bracket)

check=[0]*L
n=len(bracket)

for i in range(1,n+1):
    for com in combinations(range(1,n+1),i):
        check=[0]*L
        word=""
        for c in com:
            check[bracket[c-1][0]]=1
            check[bracket[c-1][1]]=1
        # print(check)
        for s in range(L):
            if check[s]==1:
                continue
            word+=sentence[s]
        ans.add(word)

ans=sorted(list(ans))
for a in ans:
    print(a)

