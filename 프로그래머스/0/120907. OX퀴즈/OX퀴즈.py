def solution(quiz):
    q_list = []
    answer = []
    for i in quiz:
        q_list.append(i.replace('=','=='))
    for j in q_list:
        if eval(j):
            answer.append("O")
        else:
            answer.append("X")
    return answer