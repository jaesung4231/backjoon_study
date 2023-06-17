import sys
input=sys.stdin.readline
duck=list(input().strip())
isduck=False
cnt=0

def check(a,b):
    if a=='q' and b!='u':
        return False
    elif a=='u' and b!='a':
        return False
    elif a=='a' and b!='c':
        return False
    elif a=='c' and b!='k':
        return False
    elif a=='k' and b!='q':
        return
    return True


def find(L):
    global cnt
    isduck=False
    cur=duck[L]
    pos=L
    for i in range(L,len(duck)):
        if duck[i]=='A':
            continue
        if check(cur,duck[i]):
            if cur=='c' and duck[i]=='k':
                isduck=True
            cur=duck[i]
            duck[pos]='A'
            pos=i
            duck[i]='A'
    
    if isduck==True:
        cnt+=1
    
    if cur!='k':
        cnt=0
        return
        
    for i in range(len(duck)):
        if duck[i]=='A':
            continue
        if duck[i]=='q':
            find(i)
        else:
            cnt=0
            # print(duck)
            return

    

find(0)
if cnt==0:
    print(-1)
else:
    print(cnt)



