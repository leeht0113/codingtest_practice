from collections import deque

def solution(maps):
    answer = []
    rows = len(maps)
    columns = len(maps[0])
    visited = [[0] * columns for _ in range(rows)]
    
    def bfs(start):
        queue = deque([(start[0], start[1])])
        visited[start[0]][start[1]] = 1
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        days = int(maps[start[0]][start[1]])
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < rows and 0 <= ny < columns:
                    if maps[nx][ny] != 'X' and visited[nx][ny] == 0:
                        queue.append((nx, ny))
                        visited[nx][ny] = 1
                        days += int(maps[nx][ny])
        return days 
    
    for i in range(rows):
        for j in range(columns):
            if maps[i][j] != "X" and visited[i][j] == 0:
                answer.append(bfs((i, j)))

    if len(answer) == 0:
        return [-1]
    
    answer.sort()
    return answer