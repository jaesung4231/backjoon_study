from collections import deque, defaultdict
import sys
input=sys.stdin.readline
n,m,k=map(int,input().split())
board=[]
fireball=[]

move=[[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]

def pb(board):
    for i in range(n):
        print(board[i])
    print("================")


for i in range(m):
    data=list(map(int,input().split()))
    fireball.append([data[0]-1,data[1]-1,data[2],data[3],data[4]])

def split(wait):
    for w in wait:
        mass=0
        speed=0
        isEven=True
        isOdd=True
        if len(wait[w])>1:
            for fire in wait[w]:
                mass+=fire[2]
                speed+=fire[3]
                if fire[4]%2==0:
                    isOdd=False
                else:
                    isEven=False

            if (mass//5)>0:
                if isOdd==True or isEven==True:
                    tmp=0
                    for _ in range(4):
                        fireball.append([w[0],w[1],mass//5,(speed//len(wait[w])),tmp])
                        tmp+=2
                else:
                    tmp=1
                    for _ in range(4):
                        fireball.append([w[0],w[1],mass//5,(speed//len(wait[w])),tmp])
                        tmp+=2

        else:
            fireball.append([w[0],w[1],wait[w][0][2],wait[w][0][3],wait[w][0][4]])



def go(fire,wait):
    for dir in range(8):
        if dir==fire[4]:
            nx=fire[0]
            ny=fire[1]
            for _ in range(fire[3]):
                nx=nx+(move[fire[4]][0])
                ny=ny+(move[fire[4]][1])
                if nx==-1:
                    nx=n-1
                elif nx==n:
                    nx=0
                if ny==-1:
                    ny=n-1
                elif ny==n:
                    ny=0
            wait[nx,ny].append(fire)
    


for i in range(k):
    wait=defaultdict(list)
    for fire in fireball:
        if fire[2]==0:
            continue
        go(fire,wait)
    fireball=[]
    split(wait)

answer=0
for fire in fireball:
    answer+=fire[2]

print(answer)
