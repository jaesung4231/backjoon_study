import sys
from collections import deque
input=sys.stdin.readline
N=int(input())
board=[]
dp=[]
mdp=[]
table={'*','+','-'}
cal=[[0,1],[1,0]]

for _ in range(N):
    board.append(list(map(str,input().split())))
    dp.append([-1e9]*N)
    mdp.append([1e9]*N)

dp[0][0]=int(board[0][0])
mdp[0][0]=int(board[0][0])


def pb(board):
    for b in board:
        print(b)
    print("================")

def calculate(a,b,x):
    if x=="+":
        return a+b
    elif x=="-":
        return a-b
    elif x=="*":
        return a*b

for i in range(1,N):
    if board[0][i] not in table:
        dp[0][i]=calculate(dp[0][i-2],int(board[0][i]),board[0][i-1])
        mdp[0][i]=calculate(dp[0][i-2],int(board[0][i]),board[0][i-1])

for i in range(1,N):
    if board[i][0] not in table:
        dp[i][0]=calculate(dp[i-2][0],int(board[i][0]),board[i-1][0]) 
        mdp[i][0]=calculate(dp[i-2][0],int(board[i][0]),board[i-1][0])

for i in range(1,N):
    for j in range(1,N):
        if board[i][j] not in table:
            for k in range(2):
                 dp[i][j]=max(dp[i][j], calculate(dp[i-1][j-1],int(board[i][j]),board[i-cal[k][0]][j-cal[k][1]]))
                 mdp[i][j]=min(mdp[i][j], calculate(mdp[i-1][j-1],int(board[i][j]),board[i-cal[k][0]][j-cal[k][1]]))
            if -1<j-2:
                dp[i][j]=max(dp[i][j],calculate(dp[i][j-2],int(board[i][j]),board[i][j-1]))
                mdp[i][j]=min(mdp[i][j],calculate(mdp[i][j-2],int(board[i][j]),board[i][j-1]))
            if -1<i-2:
                dp[i][j]=max(dp[i][j],calculate(dp[i-2][j],int(board[i][j]),board[i-1][j]))
                mdp[i][j]=min(mdp[i][j],calculate(mdp[i-2][j],int(board[i][j]),board[i-1][j]))

# pb(dp)
print(dp[N-1][N-1],mdp[N-1][N-1])
