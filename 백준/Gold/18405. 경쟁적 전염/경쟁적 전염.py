from collections import deque

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

virus = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            virus.append((graph[i][j], i, j))

virus.sort()
queue = deque(virus)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

time = 0
while queue and time < s:
    for _ in range(len(queue)):
        v, r, c = queue.popleft()
        for i in range(4):
            nx = r + dx[i]
            ny = c + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = v
                queue.append((v, nx, ny))
    time += 1

print(graph[x-1][y-1])