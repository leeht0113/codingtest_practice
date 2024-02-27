def solution(data, ext, val_ext, sort_by):
    answer = []
    by = ['code', 'date', 'maximum', 'remain']
    for d in data:
        if d[by.index(ext)] < val_ext:
            answer.append(d)
    answer.sort(key = lambda x: x[by.index(sort_by)])    
    return answer