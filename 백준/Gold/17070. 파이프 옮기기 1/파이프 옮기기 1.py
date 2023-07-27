import sys
import heapq
input=sys.stdin.readline
sys.setrecursionlimit(10**5)
n=int(input())
board=[]
dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(3)]
ans=0

def pb(board):
    for i in range(len(board)):
        print(board[i])
    print("===================")


for _ in range(n):
    board.append(list(map(int,input().split())))

for i in range(1,n):
    if board[0][i]==0:
        dp[0][0][i]=1
    else:
        break

for i in range(1,n):
    for j in range(1,n):
        if board[i][j]==0:
            dp[0][i][j]=dp[2][i][j-1]+dp[0][i][j-1]
            
            dp[1][i][j]=dp[2][i-1][j]+dp[1][i-1][j]

            if board[i-1][j]==0 and board[i][j-1]==0:
                dp[2][i][j]=dp[0][i-1][j-1]+dp[1][i-1][j-1]+dp[2][i-1][j-1]

# for i in range(3):
#     pb(dp[i])

ans=0
for i in range(3):
    ans+=dp[i][n-1][n-1]
print(ans)