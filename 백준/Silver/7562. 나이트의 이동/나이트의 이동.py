import sys
input = sys.stdin.readline


dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

def bfs_bound(bd, start, end):
    if start == end:
        return 0
    que = [start]
    visited = {start}
    m = 1
    while True:
        new_que = []
        for x, y in que:
            for i, j in zip(dx, dy):
                nx, ny = x+i, y+j
                if 0 <= nx < bd and 0 <= ny < bd:
                    new = nx, ny
                    if new not in visited:
                        visited.add(new)
                        new_que.append(new)
        if end in visited:
            return m
        m += 1
        que = new_que

def bfs(p):
    if p == (0, 0):
        return 0
    start = (0, 0)
    que = [start]
    visited = {start}
    for m in range(1, 10):
        new_que = []
        for x, y in que:
            for i, j in zip(dx, dy):
                new = x + i, y + j
                if new not in visited:
                    visited.add(new)
                    new_que.append(new)
        if p in visited:
            return m
        que = new_que

def manual(x, y):
    i = 0
    while x >= 5 or y >= 5:
        x, y = (x-2, abs(y-1)) if x > y else (abs(x-1), y-2)
        i += 1
    return i + bfs((x, y))

for _ in range(int(input())):
    bd = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x, y = abs(x1-x2), abs(y1-y2)
    if x >= 5 or y >= 5:
        print(manual(x, y))
    else:
        print(bfs_bound(bd, (x1, y1), (x2, y2)))