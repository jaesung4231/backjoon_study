import sys
from collections import deque, defaultdict
input=sys.stdin.readline
n=int(input())
m=int(input())
order=list(input().strip())
start=defaultdict(list)
end=defaultdict(list)
board=[]
move=[[0,-1],[0,1]]
for o in range(n):
    end[order[o]]=[m-1,o*2]
order.sort()
for o in range(n):
    start[order[o]]=[0,o*2]

for i in range(m):
    tmp=list(input().strip())
    if tmp[0]=="?":
        tmp=('?'.join(tmp))
        arr="?"
        arr+=(tmp+"?")
    else:
        tmp=('0'.join(tmp))
        arr="0"
        arr+=(tmp+"0")
    board.append(arr.strip())

def move_down(x,y):
    N=len(board)
    M=len(board[0])
    queue=deque()
    queue.append([x,y])
    visited=defaultdict(int)
    visited[x,y]
    while queue:
        a,b=queue.popleft()
        wentLeft=False
        if board[a][b]=="?":
            return [a,b]
        for i in range(2):
            nx=a
            ny=b+move[i][1]
            if -1<nx<N and -1<ny<M and board[nx][ny]=="-" and (nx,ny) not in visited:
                queue.append([nx+move[i][0],ny+move[i][1]])
                visited[nx,ny]
                wentLeft=True
                break
        if wentLeft==False:
            nx=a+1
            ny=b
            visited[nx,ny]
            queue.append([nx,ny])

def move_up(x,y):
    N=len(board)
    M=len(board[0])
    queue=deque()
    queue.append([x,y])
    visited=defaultdict(int)
    visited[x,y]
    while queue:
        a,b=queue.popleft()
        wentLeft=False
        if board[a][b]=="?":
            return [a,b]
        for i in range(2):
            nx=a
            ny=b+move[i][1]
            if -1<nx<N and -1<ny<M and board[nx][ny]=="-" and (nx,ny) not in visited:
                queue.append([nx+move[i][0],ny+move[i][1]])
                visited[nx,ny]
                wentLeft=True
                break
        if wentLeft==False:
            nx=a-1
            ny=b
            visited[nx,ny]
            queue.append([nx,ny])


ans=['*']*(n-1)

# for i in range(m):
#     print(board[i])

for i in start:
    down=(move_down(start[i][0],start[i][1]))
    up=(move_up(end[i][0],end[i][1]))
    # print(down,"d",i)
    # print(up,"up")
    if abs(down[1]-up[1])>2:
        ans=['x']*(n-1)
        break
    elif abs(down[1]-up[1])==2:
        ans[min(down[1],up[1])//2]="-"

for i in range(1,n-1):
    if ans[i-1]=="-" and ans[i]==ans[i-1]:
        ans=['x']*(n-1)
        break
txt=""
for i in range(n-1):
    txt+=ans[i]
print(txt)





