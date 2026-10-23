def solution(n):
    answer = set()
    i = 2
    while i <= n:
        if n % i == 0:
            answer.add(i)
            n = n // i
        else:
            i += 1
    return sorted(list(answer))