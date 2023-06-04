from collections import deque, defaultdict
from itertools import combinations, product, permutations
from copy import deepcopy
import heapq
import sys
input=sys.stdin.readline
n,L=map(int,input().split())
board=[]
test=[3,3,2,2,3,3]

for i in range(n):
    board.append(list(map(int,input().split())))


def pb(board):
    for i in range(len(board)):
        print(board[i])
    print("========")


def check(arr):
    path=defaultdict(int)
    for j in range(n-1):
        cost=(arr[j]-arr[j+1])
        if cost>1:
            return False
        elif cost==1:

            if j+L<n:
                canBuild=True
                for k in range(1,L):
                    if arr[j+k]!=arr[j+k+1] and (j+k) not in path:
                        canBuild=False
                        break
                if canBuild==True:
                    for k in range(1,L+1):
                        path[j+k]
                else:
                    return False
            else:
                return False
    
        if cost<-1:
            return False
        
        elif cost==-1:
            if j-L>=-1:
                canBuild=True
                for k in range(L-1):
                    # print(arr[j-k],arr[j-k-1])
                    if arr[j-k]!=arr[j-k-1]:
                        canBuild=False
                        break
                
                if canBuild==True:
                    for k in range(L):
                        if (j-k) in path:
                            return False
                else:
                    return False
            else:
                return False
    return True

ans=0

for i in range(n):
    if check(board[i][:])==True:
        ans+=1

for i in range(n):
    p=[]
    for j in range(n):
        p.append(board[j][i])
    if (check(p))==True:
        ans+=1

print(ans)

    
