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
#import sys
#sys.stdin = open("input.txt", "r")

T=int(input())

move=[
    [[1,1],[1,-1]],
    [[1,-1],[-1,-1]],
    [[-1,-1],[-1,1]],
    [[-1,1],[1,1]]
]

cnt=0
answer=0

def pb():
    for i in range(n):
        print(board[i])

def start(x,y,n):
    cango=True
    dx=[1,1,-1,-1]
    dy=[1,-1,-1,1]
    for i in range(4):
        x=x+dx[i]
        y=y+dy[i]
        if  x>=n or x<=-1 or y>=n or y<=-1:
            cango=False
            break
    return cango


def check(num,x,y,visited):
    for i in range(2):
        nx=x+move[num][i][0]
        ny=y+move[num][i][1]
        # print(nx,ny,"여기",visited)
        if -1<nx<n and -1<ny<n and (board[nx][ny]) not in visited:
            return True
    return False

def find(mm):
    if mm==[1,1]:
        return 0
    elif mm==[1,-1]:
        return 1
    elif mm==[-1,-1]:
        return 2
    elif mm==[-1,1]:
        return 3
    else:
        print("[ERROR] find")


def dfs(r,c,x,y,visited,dir):
    global cnt
    global answer
    cango=True
    visited[board[x][y]]=(x,y)
    if  r==x and c==y:
        answer=max(answer,len(visited))
        return
    if check(dir,x,y,visited)==False:
        return
    else:
        for i in range(2):
            nx=x+move[dir][i][0]
            ny=y+move[dir][i][1]
            if -1<nx<n and -1<ny<n and (board[nx][ny] not in visited) and (nx,ny) not in passed:
                visited[board[nx][ny]]=(nx,ny)
                tmp_dir=find(move[dir][i])
                dfs(r,c,nx,ny,visited,tmp_dir)
                del visited[board[nx][ny]]

for t in range(T):
    board=[]
    cnt=0
    n=int(input())
    k=n-1
    answer=-1
    visited={}
    passed={}
    for i in range(n):
        board.append(list(map(int,input().split())))
    for i in range(n):
        for j in range(n):
            visited={}
            if start(i,j,n):
                dfs(i,j,i+1,j+1,visited,0)
            passed[i,j]=1
    print(f"#{t+1}",answer)
    

    
    
