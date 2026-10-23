def solution(s):
    answer = []
    string_dict = {}
    for idx, word in enumerate(s):
        if word not in string_dict:
            answer.append(-1)
        else:
            answer.append(idx - string_dict[word])
        string_dict[word] = idx
    return answer