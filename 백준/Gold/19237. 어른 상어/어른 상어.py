from collections import deque, defaultdict
from itertools import combinations, product, permutations
from copy import deepcopy
import sys
input=sys.stdin.readline
n,m,k=map(int,input().split())
board=[]
shark=[]
smell=[]
order=[[[] for _ in range(4)] for _ in range(m)]
went=[]
move=[[0,0],[-1,0],[1,0],[0,-1],[0,1]]
cnt=m
def pb(board):
    for i in range(n):
        print(board[i])
    print("===============")

for i in range(n):    
    board.append(list(map(int,input().split())))
    smell.append([0]*n)
    went.append([0]*n)


for i in range(n):
    for j in range(n):
        if board[i][j]!=0:
            shark.append([i,j,board[i][j],0])
            smell[i][j]=k
            went[i][j]=board[i][j]


dir=(list(map(int,input().split())))


for i in range(m*4):
    data=(list(map(int,input().split())))
    order[i//4][i%4]=data


shark.sort(key=lambda x:x[2])
for i in range(m):
    shark[i][3]=dir[i]



def search(shark,wait):
    global cnt
    cang0=False
    for j in range(4):
        nx=shark[0]+move[order[shark[2]-1][shark[3]-1][j]][0]
        ny=shark[1]+move[order[shark[2]-1][shark[3]-1][j]][1]
        if -1<nx<n and -1<ny<n: 
            if smell[nx][ny]==0:
                shark[3]=order[shark[2]-1][shark[3]-1][j]
                wait[nx,ny].append(shark)
                # smell[nx][ny]=k
                # went[nx][ny]=shark[2]
                # shark[0]=nx
                # shark[1]=ny
                # shark[3]=order[shark[2]-1][shark[3]-1][j]
                return [nx,ny]
            # elif smell[nx][ny]==k:
            #     print(f"{shark[2]} came")
            #     if check(nx,ny,shark)==True:
            #         shark[3]=order[shark[2]-1][shark[3]-1][j]
            #         return [nx,ny]


    for j in range(4):
        nx=shark[0]+move[order[shark[2]-1][shark[3]-1][j]][0]
        ny=shark[1]+move[order[shark[2]-1][shark[3]-1][j]][1]  
        if -1<nx<n and -1<ny<n and went[nx][ny]==shark[2]:
            smell[nx][ny]=k
            went[nx][ny]=shark[2]
            shark[0]=nx
            shark[1]=ny
            shark[3]=order[shark[2]-1][shark[3]-1][j]
            # print(order[shark[2]-1][shark[3]-1][j])
            # print(shark[2],nx,ny,"움직임")
            return [nx,ny]

    


def check(nx,ny,rank):
    global cnt
    ate=False
    for s in range(len(shark)):
        if shark[s][2]==rank[2] or shark[s][0]==-1:
            continue
        if shark[s][0]==nx and shark[s][1]==ny:
            if shark[s][2]>rank[2]:
                shark[s][0]=-1
                went[nx][ny]=rank[2]
                # print(f"{shark[s][2]}죽음",f"{cnt-1}남음")
            else:
                rank[0]=-1
                # print(f"{rank[2]}죽음",f"{cnt-1}남음")
            cnt-=1
            ate=True
        

    return ate

def check_went():
    for i in range(n):
        for j in range(n):
            if smell[i][j]==0:
                went[i][j]==0
            

def move_all_shark():
    global cnt
    visited=defaultdict(int)
    wait=defaultdict(list)

    # pb(smell)
    # pb(went)
    for s in range(len(shark)):
        if shark[s][0]==-1:
            continue
        v=search(shark[s],wait)
        visited[tuple(v)]

    for w in wait:
        if len(wait[w])==1:
            smell[w[0]][w[1]]=k
            went[w[0]][w[1]]=wait[w][0][2]
            shark[wait[w][0][2]-1][0]=w[0]
            shark[wait[w][0][2]-1][1]=w[1]
        else:
            wait[w].sort(key=lambda x:x[2])
            # print(wait)
            # print(shark)
            for i in range(1,len(wait[w])):
                shark[wait[w][i][2]-1][0]=-1
                cnt-=1
                # print(w,wait[w][i][2],"die",cnt)
            
            smell[w[0]][w[1]]=k
            went[w[0]][w[1]]=wait[w][0][2]
            shark[wait[w][0][2]-1][0]=w[0]
            shark[wait[w][0][2]-1][1]=w[1]




   
    for i in range(n):
        for j in range(n):
            if (i,j) not in visited and smell[i][j]!=0:
                smell[i][j]-=1
                if smell[i][j]==0:
                    went[i][j]=0
            

    

    
time=0
while(1):
    if time>1000:
        print(-1)
        # print(shark)
        # pb(smell)
        # pb(went)
        break
    if cnt==1:
        print(time)
        # print(shark)
        break
    move_all_shark()  
    time+=1




