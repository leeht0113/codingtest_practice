import math

def solution(n):
    answer =[]
    for i in range(1, 11):
        if math.factorial(i) <= n:
            answer.append(i)
    return max(answer)