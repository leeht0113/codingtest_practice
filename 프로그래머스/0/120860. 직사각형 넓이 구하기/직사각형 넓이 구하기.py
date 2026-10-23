def solution(dots):
    x = [x[0] for x in dots]
    y = [y[1] for y in dots]
    width = max(x) - min(x)
    height = max(y) - min(y)
    return width * height