def solution(n):
    res = [[0] * i for i in range(1, n+1)]
    dy = -1
    dx = 0
    num = 1
    
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
            res[dy][dx] = num
            num += 1
    return [j for i in res for j in i]