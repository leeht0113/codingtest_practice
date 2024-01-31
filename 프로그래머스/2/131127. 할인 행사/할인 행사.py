def solution(want, number, discount):
    answer = 0
    want_dict = {}
    for w, n in zip(want, number):
        want_dict[w] = n
    for i in range(len(discount)):
        temp = want_dict.copy()
        if i + 10 <= len(discount):
            for d in discount[i:i+10]:
                if temp.get(d, 0) > 0:
                    temp[d] -= 1
            if sum(temp.values()) == 0:
                answer += 1
    return answer