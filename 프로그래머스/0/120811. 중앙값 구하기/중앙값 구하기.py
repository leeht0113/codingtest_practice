def solution(array):
    data = sorted(array)
    center = len(array) // 2
    if len(array)%2 > 0:
        answer = data[center]
    elif len(array)%2 == 0:
        answer = (data[center-1] + data[center])/2
    return answer