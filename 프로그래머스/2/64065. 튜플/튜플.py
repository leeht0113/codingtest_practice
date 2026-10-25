from collections import OrderedDict

def solution(s):
    answer = OrderedDict()
    s = sorted(s[2:-2].split("},{"), key = len)
    for tuples in s:
        elements = tuples.split(',')
        for element in elements:
            number = int(element)
            if number not in answer:
                answer[number] = 1
    return list(answer)