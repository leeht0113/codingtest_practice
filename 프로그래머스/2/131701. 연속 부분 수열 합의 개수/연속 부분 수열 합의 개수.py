def solution(elements):
    l = len(elements)
    answer = set()
    for i in range(l):
        temp = elements[i]
        answer.add(temp)
        for j in range(i + 1, i + l):
            temp += elements[j%l]
            answer.add(temp)
    return len(answer)