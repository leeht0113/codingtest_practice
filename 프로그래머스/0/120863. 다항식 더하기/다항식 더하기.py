import re

def solution(polynomial):
    answer = []
    p = re.compile('[0-9]*x')
    polynomial = polynomial.split(' ')
    coeff_num = 0
    numeric = 0
    for i in polynomial:
        if p.match(i):
            if len(i) == 1:
                coeff_num += 1
            else:
                coeff_num += int(i[:-1])
        elif i.isnumeric():
            numeric += int(i)
    if coeff_num > 0:
        if coeff_num == 1:
            answer.append('x')
        else:
            answer.append(str(coeff_num) + 'x')
    if numeric > 0:
        answer.append(str(numeric))
    return " + ".join(answer)