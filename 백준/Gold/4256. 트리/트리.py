import sys
input=sys.stdin.readline
T=int(input())


def search(pre,ino):
    if len(pre)==0:
        return
    elif len(pre)==1:
        print(pre[0],end=" ")
        return
    elif len(pre)==2:
        print(pre[1],pre[0],end=" ")
        return
    
    root_idx=ino.index(pre[0])

    left_in=ino[0:root_idx]
    left_pre=pre[1:len(left_in)+1]
    search(left_pre,left_in)

    right_in=ino[root_idx+1:]
    right_pre=pre[len(left_pre)+1:]
    search(right_pre,right_in)
    print(pre[0],end=' ')
    

for t in range(T):
    n=int(input())
    pre=list(map(int,input().split()))
    ino=list(map(int,input().split()))
    search(pre,ino)
    print()