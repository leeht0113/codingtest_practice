def solution(n):
    res = [[0] * i for i in range(1, n + 1)]
    dy = -1
    dx = 0
    cnt = 0
    for i in range(n):
        for _ in range(i, n):
            angle = i % 3
            if angle == 0:
                dy += 1
            elif angle == 1:
                dx += 1
            else:
                dy -= 1
                dx -= 1
            cnt += 1
            res[dy][dx] = cnt
    return [i for j in res for i in j]