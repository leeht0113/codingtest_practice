from collections import deque

def solution(board):
    queue = deque()
    row, column = len(board), len(board[0])
    # "R" 로봇의 처음 위치를 찾아서 queue에 저장
    for r in range(row):
        for j in range(column):
            if board[r][j] == 'R':
                queue.append((r, j, 0))
                break
    visited = set()
    # "R" 위치에서 시작
    visited.add((queue[0][0], queue[0][1]))
    move_row = [-1, 1, 0, 0]
    move_column = [0, 0, -1, 1]
    while queue:
        r, c, move = queue.popleft()
        # 큐에서 나온 좌표가 board의 'G'라면 이동횟수를 반환
        if board[r][c] == 'G':
            return move
        # 상하좌우로 움직임
        for n in range(4):
            new_row = r
            new_column = c
            # "D"를 만나기 전까지 같은 방향으로 움직임
            while 0 <= new_row + move_row[n] < row and 0 <= new_column + move_column[n] < column and board[new_row + move_row[n]][new_column + move_column[n]] != 'D':
                new_row += move_row[n]
                new_column += move_column[n]
            if (new_row, new_column) not in visited:
                # 멈춘 위치가 방문한 적이 없다면 queue에 추가, 이동횟수도 추가
                queue.append((new_row, new_column, move + 1))
                # 방문 set에 멈춘 위치 추가
                visited.add((new_row, new_column))
    return -1