from collections import deque

def solution(board):
    def is_valid(x, y):
        return 0 <= x < N and 0 <= y < N
    
    def is_blocked(x, y):
        return not is_valid(x, y) or board[x][y] == 1
    
    def calculate_cost(direction, prev_direction, cost):
        if prev_direction == -1 or prev_direction == direction:
            return cost + 100
        else:
            return cost + 600
    
    N = len(board)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[[float('inf')] * 4 for _ in range(N)] for _ in range(N)]
    queue = deque([(0, 0, -1, 0)])  # (x, y, direction, cost)
    for i in range(4):
        visited[0][0][i] = 0
    
    while queue:
        x, y, prev_direction, cost = queue.popleft()
        
        for direction, (dx, dy) in enumerate(directions):
            new_x, new_y = x + dx, y + dy
            
            if is_blocked(new_x, new_y):
                continue
            
            new_cost = calculate_cost(direction, prev_direction, cost)
            
            if visited[new_x][new_y][direction] > new_cost:
                visited[new_x][new_y][direction] = new_cost
                queue.append((new_x, new_y, direction, new_cost))
    return min(visited[N - 1][N - 1])
