def solution(n):
    cur = n
    while True:
        new = cur + 1
        n_cnt = bin(n).count('1')
        new_cnt = bin(new).count('1')
        if n_cnt == new_cnt:
            return new
        else:
            cur += 1
    return answer