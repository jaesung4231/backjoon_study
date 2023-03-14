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

dx=[0,-1,1,0,0]
dy=[0,0,0,-1,1]

def pb():
    for i in range(n):
        print(board[i])
    print("=================")


def kill(idx):
    if mii[idx][2]==0:
        return
    mii[idx][2]=(mii[idx][2]//2)
    if mii[idx][3]==1 or mii[idx][3]==3:
        mii[idx][3]+=1
    else:
        mii[idx][3]-=1


def combine(wait):
    for w in wait:
        total=0
        mm=0
        win_idx=-1
        # print(w,wait)
        for idx in wait[w]:
            total+=mii[idx][2]
            if mii[idx][2]>mm:
                mm=mii[idx][2]
                win_idx=idx
        board[w[0]][w[1]]=win_idx
        for idx in wait[w]:
            if idx==win_idx:
                mii[idx][0]=w[0]
                mii[idx][1]=w[1]
                mii[idx][2]=total
            else:
                mii[idx]=[0,0,0,0,0]
        # print("합친 결과",w[0],w[1],board[w[0]][w[1]],mii[win_idx])
        
        
def go(nx,ny,idx):
    if mii[idx][2]==0:
        return
    board[nx][ny]=idx
    if board[mii[idx][0]][mii[idx][1]]==idx:
        board[mii[idx][0]][mii[idx][1]]=0
    mii[idx][0]=nx
    mii[idx][1]=ny


def move(idx,time):
    if mii[idx][2]==0:
        return
    mii[idx][4]=time
    for i in range(1,5):
        if i==mii[idx][3]:
            nx=mii[idx][0]+dx[i]
            ny=mii[idx][1]+dy[i]
            if 0<nx<n-1 and 0<ny<n-1:  
                if (nx,ny) not in wait:
                    wait[nx,ny]=[idx]
                else:
                    wait[nx,ny].append(idx)
                board[mii[idx][0]][mii[idx][1]]=0
            elif nx==0 or nx==n-1 or ny==0 or ny==n-1:
                go(nx,ny,idx)
                kill(idx)
            return

                
def find_ans(dict):
    tmp=0
    for i in range(len(dict)):
        tmp+=mii[f"{i}"][2]
    return tmp


for t in range(T):
    n,m,k=map(int, input().split())
    board=[]
    mii={}
    answer=0
    for i in range(n):
        board.append([0]*n)

    for i in range(k):
        x,y,number,dir=map(int,input().split())
        mii[f"{i}"]=[x,y,number,dir,-1]
        board[x][y]=f"{i}"


    for time in range(m):
        wait={}
        # pb()
        for e in mii:
            if mii[e][2]==0:
                continue
            move(e,time)
        combine(wait)
   
    answer=find_ans(mii)
    # print(mii)
    print(f"#{t+1}",answer)
    






    
