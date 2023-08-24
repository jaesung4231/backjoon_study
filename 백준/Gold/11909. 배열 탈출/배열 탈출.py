import sys
input=sys.stdin.readline
N=int(input())
board=[]
dp=[[1e9]*N for _ in range(N)]
dp[0][0]=0

def pb(board):
    for b in board:
        print(b)
    print("============")

for _ in range(N):
    board.append(list(map(int,input().split())))

for i in range(N):
    for j in range(N):
        if i<N-1 and j<N-1:
            if board[i][j]<=board[i+1][j]:
                dp[i+1][j]=min(dp[i+1][j],dp[i][j]+(board[i+1][j]+1-board[i][j]))
            else:
                dp[i+1][j]=min(dp[i+1][j],dp[i][j])

            if board[i][j]<=board[i][j+1]:
                dp[i][j+1]=min(dp[i][j+1],dp[i][j]+(board[i][j+1]+1-board[i][j]))
            else:
                dp[i][j+1]=min(dp[i][j+1],dp[i][j])
        
        elif i==N-1 and j<N-1:
            if board[i][j]<=board[i][j+1]:
                dp[i][j+1]=min(dp[i][j+1],dp[i][j]+(board[i][j+1]+1-board[i][j]))
            else:
                dp[i][j+1]=min(dp[i][j+1],dp[i][j])
        
        elif i<N-1 and j==N-1:
            if board[i][j]<=board[i+1][j]:
                dp[i+1][j]=min(dp[i+1][j],dp[i][j]+(board[i+1][j]+1-board[i][j]))
            else:
                dp[i+1][j]=min(dp[i+1][j],dp[i][j])

print(dp[N-1][N-1])