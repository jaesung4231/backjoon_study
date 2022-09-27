import sys
N=int(input())
rope=[]
answer=[]
for i in range(N):
    rope.append(int(sys.stdin.readline()))
rope.sort()
tmp=1
for i in range(len(rope)-1,-1,-1):
    answer.append(rope[i]*(tmp))
    tmp+=1
print(max(answer))