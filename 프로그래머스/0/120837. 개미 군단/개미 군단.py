def solution(hp):
    answer = hp // 5
    hp -= 5*(hp//5)
    if hp >= 3:
        answer += hp // 3
        hp -= 3*(hp//3)
        if hp > 0:
            answer += hp // 1
            hp -= 1*(hp//1)
    else:
        answer += hp //1
        hp -= 1*(hp//1)
    return answer