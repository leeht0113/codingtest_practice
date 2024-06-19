def solution(want, number, discount):
    answer = 0
    want_dict = {}
    for w, n in zip(want, number):
        want_dict[w] = n
    for i in range(len(discount)):
        temp = want_dict.copy()
        if i + 9 < len(discount):
            for j in range(i, i + 10):
                if discount[j] in temp:
                    d = discount[j]
                    temp[d] -= 1
                    if temp[d] == 0:
                        del temp[d]
            if len(temp) == 0:
                answer += 1
    return answer