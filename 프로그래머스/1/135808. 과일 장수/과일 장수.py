def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    total_box = (len(score) // m)
    temp = [] * total_box
    for i in range(total_box):
        temp.append(score[i*m:((i*m)+m)])
    for t in temp:
        answer += min(t) * m
    return answer