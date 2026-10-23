def solution(k, score):
    answer = []
    score_list = []
    for s in score:
        if len(score_list) < k:
            score_list.append(s)
            score_list.sort(reverse=True)
            answer.append(score_list[-1])
        else:
            if s > score_list[-1]:
                score_list = score_list[:-1]
                score_list.append(s)
                score_list.sort(reverse=True)
                answer.append(score_list[-1])
            else:
                answer.append(score_list[-1])
    return answer