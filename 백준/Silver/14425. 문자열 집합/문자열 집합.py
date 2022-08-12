import sys
M_num,S_num=map(int,sys.stdin.readline().split())
M=[]
S=[]
count=0
for i in range(M_num):
  M.append(input())
for j in range(S_num):
    S=input()
    if S in M:
        count+=1
print(count)