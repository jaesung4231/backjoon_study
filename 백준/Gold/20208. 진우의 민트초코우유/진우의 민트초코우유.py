import sys
from itertools import permutations
input=sys.stdin.readline
board=[]
milk=[]
target=0
n,m,h=map(int,input().split())
for i in range(n):
    board.append(list(map(int,input().split())))


for i in range(n):
    for j in range(n):
        if board[i][j]==2:
            milk.append([i,j])
            target+=1
        elif board[i][j]==1:
            start=[i,j]

ans=0

def dfs():
    global ans
    for p in permutations(milk,len(milk)):
        cnt=0
        cur=m
        pos=start[:]
        if ans==target:
            return
        
        dis=(abs(p[0][0]-pos[0])+abs(p[0][1]-pos[1]))
        if dis>cur:
            continue


        for i in p:
            distance=abs(pos[0]-i[0])+abs(pos[1]-i[1])
            tmp=pos[:]
            if distance>cur:
                # print("can't go2")
                break
            else:
                cur-=distance
                cur+=h
                pos=i[:]
                cnt+=1
            # print(p)
            # print(tmp,pos,distance,cur,m)
        
            comeback=abs(start[0]-pos[0])+abs(start[1]-pos[1])
            if comeback<=cur:
                ans=max(ans,cnt)


dfs()
print(ans)
