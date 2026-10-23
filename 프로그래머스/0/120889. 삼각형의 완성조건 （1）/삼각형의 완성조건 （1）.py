def solution(sides):
    sides.sort()
    long = sides[-1]
    if sides[0] + sides[1] > long:
        return 1
    else:
        return 2
    return answer