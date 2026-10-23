def solution(board, moves):
    answer = 0
    dolls = [0]
    board_col = []
    for col in range(len(board[1])):
        temp = []
        for row in range(len(board)):
            if board[row][col] != 0:
                temp.append(board[row][col])
        board_col.append(temp[::-1])
    for m in moves:
        if len(board_col[m-1]) != 0:
            new = board_col[m-1].pop()
            dolls.append(new)
            top = dolls[-2]
            if new == top:
                answer += 2
                dolls = dolls[:-2]
        else:
            continue
    return answer
