# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''



'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
#sys.stdin = open("input.txt", "r")
from collections import deque,defaultdict
T=int(input())
for t in range(T):
    N,W,H=map(int,input().split())
    board=[list(map(int,input().split())) for _ in range(H)]
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    ans=W*H


    def pb(board):
        for b in board:
            print(b)
        print("==================")


    def deepcopy(board):
        tmp=[]
        for b in board:
            tmp.append(b[:])
        return tmp


    def reMake(board):
        newboard=[[0]*W for _ in range(H)]
        for i in range(W):
            tmp=[]
            for j in range(H-1,-1,-1):
                if board[j][i]!=0:
                    tmp.append(board[j][i])
                
            tmp+=[0]*(H-len(tmp))
            for j in range(H):
                if tmp[j]!=0:
                    newboard[H-j-1][i]=tmp[j]
                else:
                    break
        return newboard


    def explode(x,y,board):
        queue=deque()
        queue.append([x,y])
        visit=defaultdict(int)
        visit[x,y]
        while queue:
            a,b=queue.popleft()
            for i in range(4):
                nx=a+dx[i]
                ny=b+dy[i]
                for j in range(board[a][b]-1):
                    if -1<nx<H and -1<ny<W:
                        if (nx,ny) not in visit and board[nx][ny]!=0:
                            queue.append([nx,ny])
                    nx=nx+dx[i]
                    ny=ny+dy[i]
            board[a][b]=0
        return reMake(board) 
        


    def goDown(y,board):
        nx=0
        for _ in range(H):
            if board[nx][y]!=0:
                return (nx,y)
            nx=nx+1
        return (H-1,y)



    def count(board):
        cnt=0
        for i in range(H):
            for j in range(W):
                if board[i][j]!=0:
                    cnt+=1
        return cnt

    def dfs(p):
        global ans
        if ans==0:
            return
        if len(p)==N:
            # print(p)
            newboard=deepcopy(board)
            for i in range(N):
                x,y=goDown(p[i],newboard)
                newboard=explode(x,y,newboard)
            ans=min(ans,count(newboard))
            return
        
        for i in range(W):
            p.append(i)
            dfs(p)
            p.pop()
    p=[]
    dfs(p)
    print(f'#{t+1}',ans)
