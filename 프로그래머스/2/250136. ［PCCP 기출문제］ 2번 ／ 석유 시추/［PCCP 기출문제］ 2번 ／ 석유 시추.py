from collections import deque

group = 0 # 어느 그룹에 속하는지 표시하는 변수

def bfs(n, m, row, column, land, visited, oil):
    global group
    cnt = 1
    queue = deque()
    queue.append((n, m))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited[(n, m)] = group
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= row or ny >= column:
                continue
            if land[nx][ny] == 1 and ((nx, ny)) not in visited:
                cnt += 1
                visited[(nx, ny)] = group # 방문 좌표가 어느 그룹에 속하는지 표시
                queue.append((nx, ny))
    oil[group] = cnt
    group += 1
    
    return cnt

def solution(land):
    visited = {} # 방문 배열의 어느 덩어리에 속하는지 표시
    answer = []
    column, row = len(land[0]), len(land)
    oil = {} # 각 그룹별 석유량
    for n in range(row):
        for m in range(column):
            if (n, m) not in visited and land[n][m] == 1: # 방문한 적이 없으면 bfs 진행
                bfs(n, m, row, column, land, visited, oil)
    for m in range(column):
        group_visited = {}
        for n in range(row):
            if land[n][m] == 1:
                cur_group = visited[(n, m)] # 현재 위치가 속한 그룹
                oil_cnt = oil[cur_group] # 속한 그룹의 석유량
                if cur_group not in group_visited: # 현재 위치가 속한 그룹이 방문한 적 없던 그룹이면 추가
                    group_visited[cur_group] = oil_cnt
                else:
                    continue
        answer.append(sum(group_visited.values()))
    return max(answer)