def solution(keyinput, board):
    answer = [0, 0]
    max_x =  (board[0]-1)//2
    max_y = (board[1]-1)//2
    for i in keyinput:
        if i == "up":
            if answer[1] < max_y:
                answer[1] += 1
            else:
                continue
        elif i == "down":
            if answer[1] > -max_y:
                answer[1] -= 1
            else:
                continue
        elif i == "left":
            if answer[0] > -max_x:
                answer[0] -= 1
            else:
                continue
        elif i == "right":
            if answer[0] < max_x:
                answer[0] += 1
            else:
                continue
    return answer