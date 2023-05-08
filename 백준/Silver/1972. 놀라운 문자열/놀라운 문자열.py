import sys
from collections import defaultdict
input=sys.stdin.readline
while 1:
    arr=input().strip()
    if arr=='*':
        break
    isSup=True
    for i in range(1,len(arr)-1):
        sup=defaultdict(int)
        for l in range(len(arr)-i):
            sup[arr[l]+arr[l+i]]+=1
        for s in sup:
            if sup[s]>1:
                isSup=False
                break
        # print(sup)
        if isSup==False:
            break
            
    if isSup==True:
        print(arr+" is surprising.")
    else:
        print(arr+" is NOT surprising.")