def solution(x, n):
    start = x
    answer = [start]
    for _ in range(n-1):
        start += x
        answer.append(start)
    return answer