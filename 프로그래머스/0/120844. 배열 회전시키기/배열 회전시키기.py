def solution(numbers, direction):
    answer = []
    if direction == "right":
        answer.append(numbers[-1])
        answer += numbers[0:-1]
    elif direction == "left":
        answer.append(numbers[1])
        answer += numbers[2:]
        answer.append(numbers[0])
    return answer