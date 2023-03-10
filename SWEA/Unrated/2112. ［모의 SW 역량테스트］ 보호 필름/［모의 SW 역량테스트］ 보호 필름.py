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


# input=sys.stdin.readline
T=int(input())
def pb(board):
    for i in range(n):
        print(board[i])
    print("====================")


def check(board,k):
    for i in range(m):
        sel=0
        cnt=1
        for j in range(1,n):
            if board[j][i]==board[j-1][i]:
                cnt+=1
                sel=max(sel,cnt)
            else:
                cnt=1
        if sel<k:
            return False
    return True


def drop(num,idx,board):
    if num==0:
        for i in range(m):
            board[idx][i]=0
    elif num==1:
        for i in range(m):
            board[idx][i]=1


def dfs(L,before,board,visited,target,k):
    global ans
    visited[before]=1
    if ans!=1e9:
        return
    if L==target:
        # pb(board)
        if check(board,k):
            ans=min(ans,L)
        return
    else:
        for i in range(before,n):
            if i in visited:
                continue
            for d in range(2):
                visited[i]=1
                tmp=board[i][:]
                drop(d,i,board)
                dfs(L+1,i,board,visited,target,k)
                del visited[i]
                board[i]=tmp

for t in range(T):
    board=[]
    n,m,k=map(int,input().split())
    for i in range(n):
        board.append(list(map(int,input().split())))
    ans=1e9
    if k==1:
        print(f"#{t+1}",0)
    else:
        for i in range(k+1):
            # print(i,ans)
            visited={}
            dfs(0,-1,board,visited,i,k)
            if ans!=1e9:
                print(f"#{t+1}",ans)
                break
        
    

