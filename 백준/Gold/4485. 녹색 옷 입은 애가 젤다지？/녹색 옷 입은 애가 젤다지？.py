import sys
import heapq
input=sys.stdin.readline
sys.setrecursionlimit(10**5)

def pb(board):
    for i in range(len(board)):
        print(board[i])
    print("==============")

dx=[-1,1,0,0]
dy=[0,0,1,-1]

def dijkstra(x,y):
    distance[x][y]=board[x][y]
    queue=[]
    heapq.heappush(queue,(distance[x][y],(x,y)))
    while queue:
        dis,now=heapq.heappop(queue)
        if distance[now[0]][now[1]]!=dis: continue
        for i in range(4):
            nx=now[0]+dx[i]
            ny=now[1]+dy[i]
            if -1<nx<n and -1<ny<n:
                cost=board[nx][ny]+dis
                if distance[nx][ny]>cost+dis:
                    distance[nx][ny]=cost
                    heapq.heappush(queue,(cost,(nx,ny)))

cnt=1
while(1):
    n=int(input())
    if n==0:
        break
    board=[]
    distance=[]
    for i in range(n):
        board.append(list(map(int,input().split())))
        distance.append([1e9]*n)


    dijkstra(0,0)
    print(f'Problem {cnt}:',distance[n-1][n-1])
    cnt+=1

