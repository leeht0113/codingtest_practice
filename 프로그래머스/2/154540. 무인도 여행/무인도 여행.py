import sys

sys.setrecursionlimit(10000)

def dfs(start, maps, visited):
    x, y = start[0], start[1]
    visited[x][y] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    rows = len(maps)
    columns = len(maps[0])
    days = int(maps[x][y])
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < rows and 0 <= ny < columns:
            if maps[nx][ny] != 'X' and visited[nx][ny] == 0:
                days += dfs((nx, ny), maps, visited)
    return days

def solution(maps):
    answer = []
    rows = len(maps)
    columns = len(maps[0])
    visited = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            if maps[i][j] != 'X' and visited[i][j] == 0:
                answer.append(dfs((i, j), maps, visited))
    if len(answer) == 0:
        return [-1]
    answer.sort()
    return answer