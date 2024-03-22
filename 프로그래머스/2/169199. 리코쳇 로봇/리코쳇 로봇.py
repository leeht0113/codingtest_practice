from collections import deque

def solution(board):
    queue = deque()
    row, column = len(board), len(board[0])
    for r in range(row):
        for j in range(column):
            if board[r][j] == 'R':
                queue.append([r, j, 0])
                break
    visited = [[float('inf')] * column for _ in range(row)]
    move_row = [-1, 1, 0, 0]
    move_column = [0, 0, -1, 1]
    while queue:
        r, c, move = queue.popleft()
        if board[r][c] == 'G':
            return move
        for n in range(4):
            new_row = r
            new_column = c
            while 0 <= new_row + move_row[n] < row and 0 <= new_column + move_column[n] < column and board[new_row + move_row[n]][new_column + move_column[n]] != 'D':
                new_row += move_row[n]
                new_column += move_column[n]
            if visited[new_row][new_column] > move + 1:
                queue.append([new_row, new_column, move + 1])
                visited[new_row][new_column] = move + 1
    return -1