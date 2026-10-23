def solution(n):
    answer = 0
    for _ in range(n):
        answer += 1
        # 3의 배수이거나 숫자 3이 있으면 한번 더 1을 더함
        while answer % 3 == 0 or '3' in str(answer):
            answer += 1
    return answer