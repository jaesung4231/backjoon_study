import sys
from collections import deque
input=sys.stdin.readline
string=input().strip()

def find():
    ans=""
    tmp=""
    cur=0
    while 1:
        if cur>=len(string): break
 
        if string[cur]=="<":
            ans+=tmp[::-1]
            tmp=""
            while string[cur]!=">":
                ans+=string[cur]
                cur+=1
                if cur>=len(string): break
            ans+=string[cur]
            cur+=1
        
        elif string[cur]==" ":
            ans+=tmp[::-1]
            ans+=" "
            tmp=""
            cur+=1
        else:
            tmp+=string[cur][:]
            cur+=1

    ans+=tmp[::-1]
    return ans

print(find())        

