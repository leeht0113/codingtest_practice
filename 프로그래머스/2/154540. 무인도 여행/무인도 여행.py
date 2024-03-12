import sys

sys.setrecursionlimit(10000)

def dfs(start, maps, visited, days):
    x, y = start[0], start[1]
    visited[x][y] = 1
    move_x = [-1, 1, 0, 0]
    move_y = [0, 0, -1, 1]
    days = int(maps[x][y])
    for i in range(4):
        new_x = x + move_x[i]
        new_y = y + move_y[i]
        if 0 <= new_x < len(maps) and 0 <= new_y < len(maps[0]):
            if maps[new_x][new_y] != 'X' and visited[new_x][new_y] == 0:
                days += dfs((new_x, new_y), maps, visited, days + int(maps[new_x][new_y])) 
    return days

def solution(maps):
    answer = []
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != "X" and visited[i][j] == 0:
                answer.append(dfs((i, j), maps, visited, int(maps[i][j])))
    answer.sort()
    if len(answer) == 0:
        return [-1]
    return answer