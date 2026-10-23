from collections import Counter

def solution(X, Y):
    answer = ''
    X = Counter(X)
    Y = Counter(Y)
    for a in sorted(list(X.keys()), reverse=True):
        min_ = min(X[a], Y[a])
        answer += a * min_
    if answer == '':
        return "-1"
    elif answer[0] == '0':
        return '0'
    else:
        return answer