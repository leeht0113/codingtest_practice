def solution(s):
    answer = []
    while len(s) > 0:
        first = s[0]
        temp_dict = {s[0]:1}
        index=0
        for j in s[1:]:
            index += 1
            if j != first:
                temp_dict['others'] = temp_dict.get('others', 0) + 1
            else:
                temp_dict[first] += 1
            if temp_dict[first] == temp_dict.get('others', 0):
                answer.append(s[:index+1])
                s = s[index+1:]
                break
        if temp_dict[first] != temp_dict.get('others', 0):
            answer.append(s)
            break
    return len(answer)