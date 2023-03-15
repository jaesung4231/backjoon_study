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

ex=[0,0,0,0,0,0]
answer=1e9
def dfs(L,k):
    global answer
    if len(target)==k:
        answer=min(answer,move(target))
        return
    else:
        for i in range(L,k):
            for j in range(2):
                target.append(j)
                dfs(i+1,k)
                target.pop()

def pb(time):
    print(wait,"wait")
    for i in range(2):
        print(stair[i])
    print(f"======={time}========")


def move(target):
    time=0
    out=0
    while(1):
        for i in range(2):
            for j in stair[i]:
                if j!=[0,0] and j[0]+limit[j[1]]==time:
                    stair[i].pop(stair[i].index(j))
                    stair[i].insert(0,[0,0])
                    out+=1
                    # print("OUT",j,i,time,out)


        for i in range(2):
            if len(wait[i])!=0: 
                delete=0
                for j in wait[i]:
                    for c in range(3):
                        if stair[i][c]==[0,0] and j[0]<=time:
                            delete+=1
                            tmp=[time,j[1]]
                            stair[i][c]=tmp
                            # print("IN",tmp,time)
                            break
                for j in range(delete):
                    wait[i].pop(0)

        cnt=0
        for p in people:
            if people[p][target[cnt]]==time:
                wait[target[cnt]].append([time+1,target[cnt]])
            cnt+=1

        # pb(time)
        
        if out>len(people):
            print("ERROR")
            return time
    
        if out==len(people):
            # print(time,"시간")
            return time
        

        time+=1


for t in range(T):
    answer=1e9
    isfinished=False
    board=[]
    people={}
    s=[]
    target=[]
    cnt=0
    wait=[[],[]]
    limit=[]
    stair=[[[0,0],[0,0],[0,0]],
           [[0,0],[0,0],[0,0]]]

    n=int(input())

    for i in range(n):
        board.append(list(map(int,input().split())))
    

    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                people[i,j]=[]
            elif board[i][j]!=0:
                s.append([i,j])
                limit.append(board[i][j])
                # wait.append([0]*board[i][j])
    

    k=len(people)
    for p in people:
        for i in s:
            people[p].append(abs(i[0]-p[0])+abs(i[1]-p[1]))

    # print(people)
    dfs(0,k)
    # move(ex)
    print(f"#{t+1}",answer)
        


 
