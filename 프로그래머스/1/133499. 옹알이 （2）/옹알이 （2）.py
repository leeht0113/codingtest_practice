def solution(babbling):
    answer = 0
    babbling_list = ['aya', 'ye', 'woo', 'ma']
    for babble in babbling:
        total = ['']
        temp = ''
        for b in babble:
            temp += b
            if temp in babbling_list:
                if total[-1] != temp:
                    total.append(temp)
                    if ''.join(total[1:]) == babble:
                        answer += 1
                    else:
                        temp = ''
    return answer