def convert_base(n, base):
    """십진수 n을 base진수로 변환한다. base = 2 ~ 16"""
    digits = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
              "A", "B", "C", "D", "E", "F")
    res = ""
    while n > 0:
        n, r = divmod(n, base)
        res = digits[r] + res
    return res

def solution(n, t, m, p):
    answer = ''
    n_list = '0'
    idx = 1
    while len(n_list) <= (t * m):
        n_list += convert_base(idx, n)
        idx += 1
    # print(n_list)
    for i in range(p - 1, t * m, m):
        answer += n_list[i]
    # print(answer)
    return answer