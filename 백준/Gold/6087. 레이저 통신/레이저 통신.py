import sys
ssr = sys.stdin.readline

M, N = map(int, ssr().split())
graph = [list(ssr()[:-1]) for _ in range(N)]

start_p = [-1, -1]
end_p = [-1, -1]
for y in range(N):
    for x in range(M):
        if graph[y][x] == 'C' and start_p == [-1, -1]:
            start_p = [y, x]
            graph[y][x] = '-1'
        elif graph[y][x] == 'C':
            end_p = [y, x]
            break
    if end_p != [-1, -1]: break

from collections import deque

queue = deque()
queue.append(start_p)

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

while queue:
    y, x = queue.popleft()
    for i in range(4):
        ty = y
        tx = x
        while True:
            ty += dy[i]
            tx += dx[i]
            if 0 <= ty and ty < N and 0 <= tx and tx < M and graph[ty][tx] != '*':
                if graph[ty][tx].isdigit(): continue
                graph[ty][tx] = str(int(graph[y][x]) + 1)
                if ty == end_p[0] and tx == end_p[1]: 
                    break
                queue.append([ty, tx])
            else: break
        if graph[end_p[0]][end_p[1]] != 'C': break
    if graph[end_p[0]][end_p[1]] != 'C': break
print(int(graph[end_p[0]][end_p[1]]))