def solution(array):
    answer = []
    max_ = max(array)
    answer += [max_, array.index(max_)]
    return answer