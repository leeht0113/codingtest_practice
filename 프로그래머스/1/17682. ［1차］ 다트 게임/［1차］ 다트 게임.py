import re

def solution(dartResult):
    answer = 0
    darts = re.findall("([0-9]+)([SDT])([*#]?)", dartResult)
    num = []
    for idx, (a, b, c) in enumerate(darts):
        temp = 0
        if a.isdigit():
            temp += int(a)
        if b == 'S':
            temp = temp ** 1
        elif b == 'D':
            temp = temp ** 2
        elif b == 'T':
            temp = temp ** 3
        num.append(temp)    
        if c == "*":
            num[idx] *= 2
            if idx > 0:
                num[idx-1] *= 2
        elif c == '#':
            num[idx] *= -1
    return sum(num)