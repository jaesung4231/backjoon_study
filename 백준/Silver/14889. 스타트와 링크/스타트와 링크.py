from itertools import combinations
import sys
N=int(input())
board=[]
link=[]
start=[]
result=[]
for i in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

data=sorted(list(combinations(range(N),N//2)))
length=len(data)

for i in range(length//2):
    link.append(data[i])
    start.append(data[length-i-1])

tmp=len(link[0])

for i in range(length//2):
    combi_1=list(combinations(link[i],2))
    combi_2=list(combinations(start[i],2))
    team1=0
    team2=0
    for j in combi_1:
        team1+=(board[j[0]][j[1]]+board[j[1]][j[0]])
    for k in combi_2:
        team2+=board[k[0]][k[1]]+board[k[1]][k[0]]
    result.append(abs(team1-team2))

print(min(result),end="")