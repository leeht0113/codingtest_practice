def solution(data, ext, val_ext, sort_by):
    answer = []
    if ext == 'code':
        for d in data:
            if d[0] < val_ext:
                answer.append(d)
    elif ext == 'date':
        for d in data:
            if d[1] < val_ext:
                answer.append(d)
    elif ext == 'maximum':
        for d in data:
            if d[2] < val_ext:
                answer.append(d)
    elif ext == 'remain':
        for d in data:
            if d[3] < val_ext:
                answer.append(d)
    if sort_by == 'code':
        answer.sort(key = lambda x: x[0])
    elif sort_by == 'date':
        answer.sort(key = lambda x: x[1])
    elif sort_by == 'maximum':
        answer.sort(key = lambda x: x[2])
    elif sort_by == 'remain':
        answer.sort(key = lambda x: x[3])
    
    return answer