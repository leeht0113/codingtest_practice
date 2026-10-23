def solution(n, lost, reserve):
    u = [1] * (n + 2)
    for r in reserve:
        u[r] += 1
    for l in lost:
        u[l] -= 1
    for i in range(1, n + 1):
        if u[i - 1] == 0 and u[i] == 2:
            u[i - 1:i + 1] = [1, 1]
        elif u[i] == 2 and u[i + 1] == 0:
            u[i:i + 2] = [1, 1]
    return len([x for x in u[1:n + 1] if x > 0])