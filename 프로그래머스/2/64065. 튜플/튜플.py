def solution(s):
    s = s[2:-2].split('},{')
    s.sort(key = lambda x: len(x))
    answer = []
    exit = set()
    for numbers in s:
        n_list = numbers.split(',')
        for n in n_list:
            if n not in exit:
                answer.append(n)
                exit.add(n)
    return list(map(int, answer))