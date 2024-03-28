from collections import deque

def solution(board):
    queue = deque()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                queue.append((i, j, 0))
    visited = set((queue[0][0], queue[0][1]))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        x, y, move = queue.popleft()
        if board[x][y] == 'G':
            return move
        for i in range(4):
            new_x = x
            new_y = y
            while 0 <= new_x + dx[i] < len(board) and 0<= new_y + dy[i] < len(board[0]) and board[new_x + dx[i]][new_y + dy[i]] != 'D':
                new_x += dx[i]
                new_y += dy[i]
            if (new_x, new_y) not in visited:
                queue.append((new_x, new_y, move + 1))
                visited.add((new_x, new_y))
    return -1