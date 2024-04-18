def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key = lambda x: (x[col-1], -x[0]))
    for idx, row in enumerate(range(row_begin, row_end + 1)):
        s_i = 0
        for d in data[row - 1]:
            s_i += (d % row)
        answer ^= s_i
    return answer