import sys
import heapq
input=sys.stdin.readline
N=int(input())
pattern=input().strip()
ans=["DA","NE"]
for _ in range(N):
    word=input().strip()
    a_idx=0
    if pattern[0]=="*":
        w_idx=len(word)-1
        for i in range(len(pattern)-1,0,-1):
            if pattern[i]!=word[w_idx]:
                a_idx=1
                break
            w_idx-=1
    elif pattern[-1]=="*":
        w_idx=0
        for i in range(len(pattern)-1):
            if pattern[i]!=word[w_idx]:
                a_idx=1
                break
            w_idx+=1
    elif pattern.count("*")==0:
        if pattern!=word:
            a_idx=1
    else:
        p1=pattern.split("*")
        w_idx=0
        if (len(p1[0])+len(p1[1]))>len(word):
            a_idx=1
        else:
            w_idx=len(word)-1
            for i in range(len(pattern)-1,-1,-1):
                if pattern[i]=="*": break
                if pattern[i]!=word[w_idx]:
                    a_idx=1
                    break
                w_idx-=1
            
            w_idx=0
            for i in range(len(pattern)):
                if pattern[i]=="*": break
                if pattern[i]!=word[w_idx]:
                    a_idx=1
                    break
                w_idx+=1
            
    print(ans[a_idx])
    