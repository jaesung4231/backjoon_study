import sys
from collections import deque
input=sys.stdin.readline
r,c=map(int,input().split())
board=[]
visited_r=[]
visited_d=[]
word=""


for i in range(r):
    board.append(list(input().strip()))
    visited_r.append([0]*c)
    visited_d.append([0]*c)

# for i in range(r):
#     print(board[i])

def move_right(x,y):
    global word
    queue=deque()
    queue.append([x,y])
    visited_r[x][y]=1
    tmp=f"{board[x][y]}"
    while queue:
        a,b=queue.popleft()
        nx=a
        ny=b+1
        if ny<c and visited_r[nx][ny]==0 and board[nx][ny]!="#":
            visited_r[nx][ny]=1
            tmp+=board[nx][ny]
            queue.append([nx,ny])
    
    if len(word)==0 or (len(tmp)>=2 and tmp<word):
        word=tmp


def move_down(x,y):
    global word
    queue=deque()
    queue.append([x,y])
    visited_d[x][y]=1
    tmp=f"{board[x][y]}"
    while queue:
        a,b=queue.popleft()
        nx=a+1
        ny=b
        if nx<r and visited_d[nx][ny]==0 and board[nx][ny]!="#":
            visited_d[nx][ny]=1
            tmp+=board[nx][ny]
            queue.append([nx,ny])
    
    if len(word)==0 or (len(tmp)>=2 and tmp<word):
        word=tmp



for i in range(r):
    for j in range(c):
        if visited_r[i][j]==0 and board[i][j]!="#":
            move_right(i,j)

for i in range(r):
    for j in range(c):
        if visited_d[i][j]==0 and board[i][j]!="#":
            move_down(i,j)

print(word)