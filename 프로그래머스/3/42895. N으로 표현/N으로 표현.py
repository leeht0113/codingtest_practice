def solution(N, number):
    # N을 사용한 횟수의 결과물을 담을 dp 배열
    # 같은 숫자가 중복으로 저장되지 않기 위해 set() 사용
    dp = [set() for _ in range(9)]
    for i in range(1, 9):
        case = dp[i]
        case.add(int(str(N) * i))
        for j in range(1, i):
            # print(j, i-j)
            for op1 in dp[j]:
                for op2 in dp[i-j]:
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    if op2 != 0:
                        dp[i].add(op1 // op2)
        if number in dp[i]:
            return i
    return -1        