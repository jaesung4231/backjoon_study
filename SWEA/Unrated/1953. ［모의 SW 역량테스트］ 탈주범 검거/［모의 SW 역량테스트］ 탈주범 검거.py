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
board=[]
gomap=[]
pipe=[
    [],
    [[1,0],[-1,0],[0,1],[0,-1]],
    [[1,0],[-1,0]],
    [[0,1],[0,-1]],
    [[0,1],[-1,0]],
    [[0,1],[1,0]],
    [[0,-1],[1,0]],
    [[0,-1],[-1,0]]
]

def findGo(dir,b):
    canGo=False
    if dir=='r' and (b==1 or b==6 or b==7 or b==3):
        canGo=True
    elif dir=='l' and (b==1 or b==3 or b==5 or b==4):
        canGo=True
    elif dir=='u' and (b==1 or b==5 or b==6 or b==2):
        canGo=True
    elif dir=='d' and (b==1 or b==2 or b==4 or b==7):
        canGo=True
    return canGo

def check(b,c):
    dir=0
    if b==0:
        return False
    if c==[0,1]:
        dir='r'
    elif c==[0,-1]:
        dir='l'
    elif c==[1,0]:
        dir='d'
    elif c==[-1,0]:
        dir='u'
    else:
        print("ERROR c",c)
    return findGo(dir,b)
        
def bfs(x,y,time):
    queue=[]
    visited={}
    queue.append([x,y])
    gomap[x][y]=1
    visited[x,y]=1
    cnt=0
    answer=0
    while queue:
        a,b=queue.pop(0)
        ty=pipe[board[a][b]]
        for i in range(len(ty)):
            nx=a+ty[i][0]
            ny=b+ty[i][1]
            if -1<nx<n and -1<ny<m and check(board[nx][ny],ty[i]) and (nx,ny) not in visited:
                if gomap[a][b]<time:
                    queue.append([nx,ny])
                    gomap[nx][ny]=gomap[a][b]+1
                    visited[nx,ny]=1
                    answer+=1
        cnt+=1
    return answer+1


for i in range(T):
    n,m,r,c,time=map(int,input().split())
    ans=0
    gomap=[]
    board=[]
    for j in range(n):
        board.append(list(map(int,input().split())))
        gomap.append([0]*m)
    ans=bfs(r,c,time)
    print(f"#{i+1}", ans)
