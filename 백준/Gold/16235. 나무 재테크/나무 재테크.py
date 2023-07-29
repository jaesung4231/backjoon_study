import sys
from collections import  deque
input=sys.stdin.readline


N,M,K=map(int,input().split())
board=[]
tree=[[deque() for _ in range(N)] for _ in range(N)]
winter=[]
near=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

for i in range(N):
    board.append([5]*N)
    winter.append(list(map(int,input().split())))

for i in range(M):
    x,y,z=map(int,input().split())
    tree[x-1][y-1].append(z)


def spring(x,y):
    # 봄
    dead=0
    new_tree=deque()
    for t in tree[x][y]:
        if board[x][y]<t:
            dead+=t//2
        else:
            new_tree.append(t+1)
            board[x][y]-=t

    board[x][y]+=dead     
    tree[x][y]=new_tree


def fall(x,y):
    for t in tree[x][y]:
        if t%5==0:
            for n in near:
                nx=x+n[0]
                ny=y+n[1]
                if -1<nx<N and -1<ny<N:
                    new.append([nx,ny])
  

for k in range(K):
    new=[]
    #  봄
    for i in range(N):
        for j in range(N):
            if len(tree[i][j])!=0:
                spring(i,j)

    # 가을
    for i in range(N):
        for j in range(N):
            if len(tree[i][j])!=0:
            #    tree[i][j].sort()
               fall(i,j)
    
    for n in new:
        tree[n[0]][n[1]].appendleft(1)

    # 겨울
    for i in range(N):
        for j in range(N):
            board[i][j]+=winter[i][j]


ans=0

for i in range(N):
    for j in range(N):
        ans+=len(tree[i][j])

print(ans)

  





        



        
    




