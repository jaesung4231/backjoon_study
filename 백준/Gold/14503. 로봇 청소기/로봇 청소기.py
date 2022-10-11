import sys
input=sys.stdin.readline
N,M=map(int,input().split())
now=list(map(int,input().split()))
board=[]
for i in range(N):
    board.append(list(map(int,input().split())))

# 0 위 1 오른쪽 2 아래 3 왼쪽
def turn_left(robot):
    if robot[2]==0:
        robot[2]=3
    elif robot[2]==1:
       robot[2]=0
    elif robot[2]==2:
       robot[2]=1
    else:
       robot[2]=2

def move_for(robot):
    if robot[2]==0:
        robot[0]-=1
    elif robot[2]==1:
        robot[1]+=1
    elif robot[2]==2:
        robot[0]+=1
    elif robot[2]==3:
        robot[1]-=1

def move_back(robot):
    if robot[2]==0:
        robot[0]+=1
    elif robot[2]==1:
        robot[1]-=1
    elif robot[2]==2:
        robot[0]-=1
    elif robot[2]==3:
        robot[1]+=1

def clean(board,now):
    x=now[0]
    y=now[1]
    board[x][y]=2

def check(board,now):
    x=now[0]
    y=now[1]
    if board[x][y]==0:
        return True
    else:
        return False
answer=0
while(1):
    x=now[0]
    y=now[1]
    if board[x][y]==0:
        answer+=1
        clean(board,now)

    cnt=0
    for i in range(4):
        turn_left(now)
        move_for(now)
        if check(board,now)==True:
            break
        else:
            move_back(now)
            cnt+=1
    if cnt==4:
        move_back(now)
        if board[now[0]][now[1]]==1:
            break
    # print("=============================")
    # print("=============================")
    # print("currnt:",now)
    # for i in board:
    #     print(i)
    
# answer=0
# for i in board:
#     answer+=i.count(2)
print(answer,end="")