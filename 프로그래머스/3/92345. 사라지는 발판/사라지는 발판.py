def is_valid_pos(x, y, board):
    return 0 <= x < len(board) and 0 <= y < len(board[0])

def dfs(aloc, bloc, visited, step, board):
    if step % 2 == 0:
        x, y = aloc
    else:
        x, y = bloc
    can_move = False
    is_opponent_winner = True
    # 상대 플레이어가 이긴 경우의 이동횟수, 상대 플레이어가 진 경우의 이동횟수
    win_steps, lose_steps = [], []
    move_x = [-1, 1, 0, 0]
    move_y = [0, 0, -1, 1]
    for i in range(4):
        new_x, new_y = x + move_x[i], y + move_y[i]
        if is_valid_pos(new_x, new_y, board) and (new_x, new_y) not in visited and board[new_x][new_y]:
            can_move = True
            if aloc == bloc:
                return True, step + 1
            if step % 2 == 0:
                win, steps_left = dfs([new_x, new_y], bloc, visited | {(x, y)}, step + 1, board)
            else:
                win, steps_left = dfs(aloc, [new_x, new_y], visited | {(x, y)}, step + 1, board)
            # 한 번이라도 상대 플레이어가 지면 해당 값을 False로 만듦
            is_opponent_winner &= win
            if win:
                win_steps.append(steps_left)
            else:
                lose_steps.append(steps_left)
    # 현재 플레이어가 더 이상 이동할 수 없으면 현재 플레이어가 진 것과 같음
    if not can_move:
        return False, step
    # 상대 플레이어가 이긴 경우 패배한 플레이어는 최선을 다하므로 win_steps의 최댓값을 반환
    if is_opponent_winner:
        return False, max(win_steps)
    # 상대 플레이어가 이길 수도 있고 질 수도 있음, 현재 플레이어는 무조건 이기는 경우를 택함
    # 가장 짧은 이동 횟수로 이겨야 하므로 lose_steps의 최솟값을 택함
    return True, min(lose_steps)

def solution(board, aloc, bloc):
    _, steps = dfs(aloc, bloc, set(), 0, board)
    return steps