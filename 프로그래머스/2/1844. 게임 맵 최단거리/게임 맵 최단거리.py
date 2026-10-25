from collections import deque

def solution(maps):
    rows, columns = len(maps), len(maps[0])
    visited = [[0] * columns for _ in range(rows)]
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    queue = deque([(0, 0)])
    visited[0][0] = 1
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            move_y = y + dy[i]
            move_x = x + dx[i]
            if 0 <= move_y < rows and 0 <= move_x < columns:
                if maps[move_y][move_x] == 1 and visited[move_y][move_x] == 0:
                    visited[move_y][move_x] = visited[y][x] + 1
                    queue.append((move_y, move_x))
    result = visited[rows-1][columns-1]
    return result if result else -1