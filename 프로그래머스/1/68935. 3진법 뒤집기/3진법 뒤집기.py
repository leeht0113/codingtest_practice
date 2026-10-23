def solution(n):
    tri = []
    while n >= 1:
        tri.append(n % 3)
        n = n // 3
    answer = 0
    tri.reverse()
    for i in range(len(tri)):
        answer += ((3**(i))*tri[i])
    return answer