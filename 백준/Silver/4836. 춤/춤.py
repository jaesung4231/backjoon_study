import sys
from collections import  deque
from itertools import combinations
input=sys.stdin.readline

def check(word,ERROR):
    if len(word)<3:
        ERROR.add(2)
    else:
        if word[-1]!="clap" or word[-2]!="stomp" or word[-3]!="clap":
            ERROR.add(2)

    isDip=False
    for i in range(len(word)):
        if word[i]=="dip":
            isDip=True
       
            if i>0 and word[i-1]=="jiggle":
                continue
            if i>1 and word[i-2]=="jiggle":
                continue
            if i<len(word)-1 and word[i+1]=="twirl":
                continue
            word[i]="DIP"
            ERROR.add(1)
        
        elif word[i]=="twirl" and "hop" not in word:
            ERROR.add(3)
        elif word[i]=="jiggle" and i==0:
            ERROR.add(4)
    if isDip==False:
        ERROR.add(5)
        



while True:
    try:
        dance=input().split()
        ERROR=set()
        if len(dance)==0:
            break
        else:
            check(dance,ERROR)
            ERROR=list(ERROR)
            ans="form"
            if len(ERROR)==0:
                ans+=" ok"
            else:
                if len(ERROR)==1:
                    ans+=" error"
                    ans+=f" {ERROR[0]}"
                else:
                    ans+=" errors"
                    if len(ERROR)>2:
                        for i in range(len(ERROR)-2):
                            ans+=f" {ERROR[i]},"
                        ans+=f" {ERROR[-2]} and {ERROR[-1]}"
                    else:
                        ans+=f" {ERROR[0]} and {ERROR[1]}"
            ans+=":"
            for d in dance:
                ans+=" "
                ans+=d
            print(ans)
            
    except EOFError:
        break