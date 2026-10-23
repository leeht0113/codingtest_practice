def solution(numbers):
    n = len(numbers)
    stack = []
    answer = [-1] * n
    for i in range(n):
        value = numbers[i]
        while stack and numbers[stack[-1]] < value:
            answer[stack.pop()] = value
        stack.append(i)
    return answer