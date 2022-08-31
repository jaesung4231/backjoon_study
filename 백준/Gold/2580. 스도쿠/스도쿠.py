import sys
row=[]
box=[[]]
table={1,2,3,4,5,6,7,8,9}
blank=[]
for i in range(9):
    row.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(9):
    for j in range(9):
        if row[i][j]==0:
            blank.append((i,j))

def search_row(x,value):
    for i in range(9):
        if value==row[x][i]:
            return False
    return True

def search_col(y,value):
    for i in range(9):
        if value==row[i][y]:
            return False
    return True

def search_box(x,y,value):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if value == row[nx+i][ny+j]:
                return False
    return True

def dfs(idx):
    if idx==len(blank):
        for i in range(9):
            print(*row[i])
        exit(0)

    for i in range(1,10):
        x=blank[idx][0]
        y=blank[idx][1]
        if search_row(x,i) and search_col(y,i) and search_box(x,y,i):
                row[x][y]=i
                dfs(idx+1)
                row[x][y]=0
               
dfs(0)