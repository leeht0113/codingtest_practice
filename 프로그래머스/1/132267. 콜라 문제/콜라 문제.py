def solution(a, b, n):
    answer = 0
    while n >= a:
        answer += (n // a) * b
        # print(answer)
        n = (n // a) * b + (n % a)
        # print(n)
    return answer