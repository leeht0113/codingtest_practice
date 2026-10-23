def solution(survey, choices):
    answer = []
    total_dict = {}
    points = {1:3, 2:2, 3:1, 4:0, 5:1, 6:2, 7:3}
    metrics = ['RT', 'CF', 'JM', 'AN']
    for s, c in zip(survey, choices):
        disagree = s[0]
        agree = s[1]
        if c >=5:
            total_dict[agree] = total_dict.get(agree, 0) + points[c]
            total_dict[disagree] = total_dict.get(disagree, 0)
        elif c > 0 and c < 4:
            total_dict[disagree] = total_dict.get(disagree, 0) + points[c]
            total_dict[agree] = total_dict.get(agree, 0)
        else:
            total_dict[agree] = total_dict.get(agree, 0)
            total_dict[disagree] = total_dict.get(disagree, 0)
    for m in metrics:
        if total_dict.get(m[0], 0) > total_dict.get(m[1], 0):
            answer.append(m[0])
        elif total_dict.get(m[0], 0) < total_dict.get(m[1], 0):
            answer.append(m[1])
        else:
            answer.append(m[0])
    return ''.join(answer)