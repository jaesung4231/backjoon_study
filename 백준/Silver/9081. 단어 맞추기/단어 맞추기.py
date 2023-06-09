import sys
from collections import defaultdict
from itertools import permutations
input=sys.stdin.readline
T=int(input())

def nextpermutation(arr):
    i=len(arr)-2
    while i>=0 and arr[i]>=arr[i+1]:
        i-=1
    if i ==-1:
        return False
    
    j=len(arr)-1

    while arr[i]>=arr[j]:
        j-=1

    arr[i], arr[j] = arr[j], arr[i]

    result = arr[:i+1]
    result.extend(list(reversed(arr[i+1:])))
    return result
    


for t in range(T):
    word=list(input().strip())
    ans=(nextpermutation(word))
    if ans:
        tmp=""
        for i in range(len(word)):
            tmp+=ans[i]
        print(tmp)
    else:
        tmp=""
        for i in range(len(word)):
            tmp+=word[i]
        print(tmp)





