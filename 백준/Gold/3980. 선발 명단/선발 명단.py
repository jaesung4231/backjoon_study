import sys
from collections import defaultdict
input=sys.stdin.readline
T=int(input())
ans=0
cnt=0

p=[]
def dfs(L,lineup,member):
    global ans
    if L==11:
        total=0
        for i in range(11):
            total+=stats[member[i]][i]
        ans=max(ans,total)
        # print(member)
        return

    for player in formation[L]:
        if lineup[player]==0:
            lineup[player]=1
            member.append(player)
            dfs(L+1,lineup,member)
            member.pop()
            lineup[player]=0
        else:
            continue
    return


for t in range(T):
    ans=0
    formation=[[] for _ in range(11)]
    lineup=[0]*(11)
    member=[]
    stats=[]


    for i in range(11):
        stat=list(map(int,input().split()))
        stats.append(stat)
        for s in range(11):
            if stat[s]!=0:
                formation[s].append(i)


    # print(formation)
    dfs(0,lineup,member)
    print(ans)

