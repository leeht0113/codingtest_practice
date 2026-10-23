from collections import deque

def solution(dirs):
    # 위, 아래, 오른쪽, 왼쪽
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    queue = deque(list(dirs))
    x, y = 0, 0
    answer = 0
    route_map = []
    while queue:
        direction = queue.popleft()
        if direction == 'U':
            new_x = x + dx[0]
            new_y = y + dy[0]
        elif direction == 'D':
            new_x = x + dx[1]
            new_y = y + dy[1]
        elif direction == 'R':
            new_x = x + dx[2]
            new_y = y + dy[2]
        elif direction == 'L':
            new_x = x + dx[3]
            new_y = y + dy[3]
        if -5 <= new_x < 6 and -5 <=new_y < 6:
            route_map.append((x, y, new_x, new_y))
            route_map.append((new_x, new_y, x, y))
            x = new_x
            y = new_y
    route_map_set = set(route_map)
    return len(route_map_set)//2