def solution(s):
    s = s[2:-2].split('},{')
    s.sort(key = lambda x: len(x))
    answer = []
    exist = set()
    for numbers in s:
        n_list = numbers.split(',')
        for n in n_list:
            if n not in exist:
                answer.append(n)
                exist.add(n)
    return list(map(int, answer))