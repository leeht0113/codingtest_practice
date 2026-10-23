def divisor(n):
    count = 0
    for i in range(1, n+1):
        if n %i == 0:
            count += 1
    if count >= 3:
        return 1

def solution(n):
    answer = 0
    for i in range(1, n+1):
        if divisor(i):
            answer += 1
    return answer