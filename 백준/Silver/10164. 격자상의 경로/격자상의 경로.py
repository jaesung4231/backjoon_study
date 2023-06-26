import sys
input=sys.stdin.readline
n,m,o=map(int,input().split())
total=0
move=[[0,1],[1,0]]
ans=0
ans2=0

def find(x,y,tx,ty):
    global ans
    if x==tx and y==ty:
        ans+=1
        return
    for i in range(2):
        nx=x+move[i][0]
        ny=y+move[i][1]
        if -1<nx<=tx and -1<ny<=ty:
            find(nx,ny,tx,ty)


def find2(x,y,tx,ty):
    global ans2
    if x==tx and y==ty:
        ans2+=1
        return
    for i in range(2):
        nx=x+move[i][0]
        ny=y+move[i][1]
        if -1<nx<=tx and -1<ny<=ty:
            find2(nx,ny,tx,ty)

if o>0 and o!=(n*m):
    x=o//m
    y=o%m-1
    if y<0: 
        y=m-1
        x-=1
    board=[]
    find(0,0,x,y)
    find2(x,y,n-1,m-1)
    
    print(ans*ans2)

else:
    find(1,1,n,m)
    print(ans)
