def solution(n, words):
    answer = []
    temp = [words[0]]
    word_set = set(temp)
    # print(word_set)
    index = 0
    for idx, w in enumerate(words[1:], start = 1):
        if temp[idx - 1][-1] != w[0]:
            index = idx + 1
            break
        else:
            if w in word_set:
                index = idx + 1
                break
        temp.append(w)
        word_set.add(w)
    # print(index)
    if index == 0:
        return [0, 0]
    else:
        number = index % n
        if number == 0:
            number = n
        answer.append(number)
        turn = index / n
        if turn == int(turn):
            answer.append(int(turn))
        else:
            answer.append(int(turn) + 1)
    return answer