def block(i, j, board):
    temp = [board[i][j]]
    for a, b in [[0, 1], [1, 0], [1, 1]]:
        if i + a < len(board) and j + b < len(board[0]):
            n = board[i + a][j + b]
            if temp[-1] == n and temp[-1] != []:
                temp.append(n)
    if len(temp) == 4:
        return True
    else:
        return False

def solution(m, n, board):
    answer = 0
    # print(block(1, 1, board))    
    for i in range(m):
        board[i] = list(board[i])
    def erase(board):
        temp = []
        for i in range(m):
            for j in range(n):
                if block(i, j, board):
                    # print(i, j)
                    temp.append([i, j])
        return temp
    erase_blocks = erase(board)
    # print(board)
    # print(erase_blocks)
    remove = set()
    while len(erase_blocks) != 0:
        for a, b in erase_blocks:
            remove.add((a, b))
            remove.add((a, b + 1))
            remove.add((a + 1, b))
            remove.add((a + 1, b + 1))
        if remove:
            answer += len(remove)
            for i, j in remove:
                board[i][j] = []
            remove = set()
        else:
            break
        while True:
            moved = 0
            for i in range(m - 1):
                for j in range(n):
                    if board[i][j] and board[i + 1][j] == []:
                        board[i + 1][j] = board[i][j]
                        board[i][j] = []
                        moved = 1
            if moved == 0:
                break
        erase_blocks = erase(board)
    return answer