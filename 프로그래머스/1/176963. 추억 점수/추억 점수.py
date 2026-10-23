def solution(name, yearning, photo):
    yearning_dict = dict(zip(name, yearning))
    answer = []
    for p in photo:
        y_p = 0
        for n in p:
            y_p += yearning_dict.get(n, 0)
        answer.append(y_p)
    return answer