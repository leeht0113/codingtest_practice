def solution(s):
    answer = 0
    numbers = s.split(" ")
    for i in range(len(numbers)):
        if numbers[i] == 'Z':
            answer -= int(numbers[i-1])
        else:
            answer += int(numbers[i])
    return answer