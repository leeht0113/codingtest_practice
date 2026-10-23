def solution(names):
    answer = []
    for i in range(0, len(names), 5):
        print(i)
        answer.append(names[i])
    return answer