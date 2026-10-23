def solution(food):
    answer = ''
    for idx, f in enumerate(food):
        if idx > 0:
            answer += ''.join(str(idx) * (f//2))
    return answer + '0' + answer[::-1]