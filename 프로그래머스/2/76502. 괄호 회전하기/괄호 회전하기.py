from collections import deque

def solution(s):
    answer = 0
    s = deque(list(s))
    for i in range(len(s)):
        if i != 0:
            s.rotate(-1)
        temp = ''.join(s)
        while True:
            original = len(temp)
            temp = temp.replace('()', '')
            temp = temp.replace('{}', '')
            temp = temp.replace('[]', '')
            if len(temp) == 0:
                answer += 1
                break
            elif len(temp) == original:
                break
    return answer