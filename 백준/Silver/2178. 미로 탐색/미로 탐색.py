from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0] * m for _ in range(n)]
visited[0][0] = 1
queue = deque([[0, 0]])
while queue:
    x, y = queue.popleft()
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if 0 <= new_x < n and 0 <= new_y < m:
            if graph[new_x][new_y] == 1 and visited[new_x][new_y] == 0:
                queue.append([new_x, new_y])
                visited[new_x][new_y] = visited[x][y] + 1
print(visited[n - 1][m - 1])