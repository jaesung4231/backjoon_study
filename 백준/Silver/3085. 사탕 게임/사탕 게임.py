import sys
from itertools import combinations
input=sys.stdin.readline
N=int(input())
board=[list(input().strip()) for _ in range(N)]
col=[[]for _ in range(N)]
color=['C','P','Z','Y']
dx=[-1,1,0,0]
dy=[0,0,1,-1]
ans=1

def check(arr):
    cnt=1
    most=1
    for i in range(N-1):
        if arr[i]==arr[i+1]:
            cnt+=1
            most=max(most,cnt)
        else:
            cnt=1
    return most

for i in range(N):
    for j in range(N):
        col[j].append(board[i][j])
        tmp=board[i][j]
        ans=max(ans,check(board[i]))
        for k in range(4):
            nx=i+dx[k]
            ny=j+dy[k]
            if -1<nx<N and -1<ny<N and board[nx][ny]!=board[i][j]:
                tmp=board[i][j]
                board[i][j]=board[nx][ny]
                board[nx][ny]=tmp
                ans=max(ans,check(board[i]))
                board[nx][ny]=board[i][j]
                board[i][j]=tmp

for i in range(N):
    for j in range(N):
        ans=max(ans,check(board[i]))
        for k in range(4):
            nx=i+dx[k]
            ny=j+dy[k]
            if -1<nx<N and -1<ny<N and col[nx][ny]!=col[i][j]:
                tmp=col[i][j]
                col[i][j]=col[nx][ny]
                col[nx][ny]=tmp
                ans=max(ans,check(col[i]))
                col[nx][ny]=col[i][j]
                col[i][j]=tmp
                

print(ans)
    

        




    
    


