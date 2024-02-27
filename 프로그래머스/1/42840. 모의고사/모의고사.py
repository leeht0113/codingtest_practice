def solution(answers):
    answer = [0, 0, 0]
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    result = []
    for idx, a in enumerate(answers):
        if student1[idx%len(student1)] == a:
            answer[0] += 1
        if student2[idx%len(student2)] == a:
            answer[1] += 1
        if student3[idx%len(student3)] == a:
            answer[2] += 1
    for idx, a in enumerate(answer):
        if a == max(answer):
            result.append(idx + 1)
    return result