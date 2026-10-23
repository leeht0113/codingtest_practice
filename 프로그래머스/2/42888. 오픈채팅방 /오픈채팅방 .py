def solution(record):
    answer = []
    record = [r.split() for r in record]
    id_name = {}
    for r in record:
        if r[0] == 'Enter' or r[0] == 'Change':
            id_name[r[1]] = r[2]
    for r in record:
        if r[0] == 'Enter':
            answer.append(f'{id_name[r[1]]}님이 들어왔습니다.')
        elif r[0] == 'Leave':
            answer.append(f'{id_name[r[1]]}님이 나갔습니다.')
    return answer