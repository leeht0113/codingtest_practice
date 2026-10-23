def solution(board):
    safe = 0
    # board의 행과 열 
    r_max, c_max = len(board), len(board[0])
    for r_idx in range(r_max):
        for c_idx in range(c_max):
            # 시계방향으로 안전지대인지 탐색
            dirs = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))
            if board[r_idx][c_idx] == 0:
                # 안전지대이면 is_safe = True로 지정
                is_safe = True
                for r_mov, c_mov in dirs:
                    # 현재 위치에 각 dirs의 위치를 더함
                    r_check, c_check = r_idx + r_mov, c_idx + c_mov
                    # board 범위 안에 있는지 탐색
                    if r_check in range(r_max) and c_check in range(c_max):
                        # 탐색한 범위에 지뢰가 있으면 안전지대가 아님 (False로 변경)
                        if board[r_check][c_check] == 1:
                            is_safe = False
                # 탐색한 범위에 지뢰가 없으면 안전지대임, 안전한 지역의 칸 수로 더함
                if is_safe:
                    safe += 1
    return safe