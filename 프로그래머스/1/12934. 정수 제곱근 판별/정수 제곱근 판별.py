import math

def solution(n):
    a = int(math.sqrt(n))
    b = math.sqrt(n)
    if a == b:
        return (a + 1)**2
    else:
        return -1