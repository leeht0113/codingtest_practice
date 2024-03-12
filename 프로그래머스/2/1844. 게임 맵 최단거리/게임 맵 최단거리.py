from collections import deque

def solution(maps):
    answer = 0
    # 상, 하, 좌, 우
    move_x = [-1, 1, 0, 0]
    move_y = [0, 0, -1, 1]
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    start = (0, 0)
    visited[start[0]][start[1]] = 1
    queue = deque()
    queue.append(start)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + move_x[i]
            ny = y + move_y[i]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                if maps[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
    answer = visited[len(maps)-1][len(maps[0])-1]
    if answer != 0:
        return answer
    else:
        return -1