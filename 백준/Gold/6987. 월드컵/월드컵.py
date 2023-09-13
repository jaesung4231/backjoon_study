import sys
from itertools import combinations
games=[]
teams=[]
answer=[]
def deepcopy(team):
    tmp=[]
    for t in team:
        tmp.append(t[:])
    return tmp

def check(team):
    for t in team:
        if sum(t)!=0: return False
    return True

def dfs(L,teams):
    global ans
    if check(teams):
        ans=1
        return
    if L>=len(games):
        return
    for j in range(3):
        if teams[games[L][0]][j]>0 and teams[games[L][1]][2-j]>0:
            teams[games[L][0]][j]-=1
            teams[games[L][1]][2-j]-=1
            dfs(L+1,deepcopy(teams))
            teams[games[L][0]][j]+=1
            teams[games[L][1]][2-j]+=1

for c in combinations(range(6),2):
    games.append([c[0],c[1]])

for t in range(4):
    ans=0
    teams=[]
    tmp=list(map(int,input().split()))
    for i in range(0,18,3):
        teams.append(tmp[i:i+3])
    dfs(0,teams)
    answer.append(ans)
print(*answer)



