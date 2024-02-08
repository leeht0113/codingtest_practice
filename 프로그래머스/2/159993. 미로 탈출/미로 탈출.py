from collections import deque

def bfs(start, end, maps):
    # 방문 배열
    visited = [[0] * len(maps[0]) for _ in range(len(maps))] 
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append(start)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            # 좌표가 maps 범위에 벗어나지 않는 경우
            if 0 <= new_x < len(maps) and 0 <= new_y < len(maps[0]):
                # 처음 방문하거나 'X'가 아닌 경우 탐색 진행
                if visited[new_x][new_y] == 0 and maps[new_x][new_y] != "X":
                    visited[new_x][new_y] = visited[x][y] + 1
                    queue.append([new_x, new_y])
                    if new_x == end[0] and new_y == end[1]:
                        return visited[end[0]][end[1]]
    return visited[end[0]][end[1]]
                    
    
def solution(maps):
    # 시작 지점, 레버, 출구 좌표 구하기
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "S":
                start = [i, j]
            elif maps[i][j] == "L":
                lever = [i, j]
            elif maps[i][j] == "E":
                exit = [i, j]
    lever_exit = bfs(lever, exit, maps)
    start_lever = bfs(start, lever, maps)
    if start_lever and lever_exit:
        return start_lever + lever_exit
    else:
        return -1