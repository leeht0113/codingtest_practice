def solution(N, number):
    # N을 사용한 횟수의 결과물을 담을 dp 배열
    # 같은 숫자가 중복으로 저장되지 않기 위해 set() 사용
    dp = [set() for _ in range(9)]
    for i in range(1, 9):
        case = dp[i]
        # 숫자 N을 연속으로 반복되는 숫자 ex. 555
        case.add(int(str(N) * i))
        for j in range(1, i):
            # 총 3번 숫자를 사용 했으면
            # (1, 2), (2, 1)
            # print(j, i-j)
            for op1 in dp[j]:
                for op2 in dp[i-j]:
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    if op2 != 0:
                        dp[i].add(op1 // op2)
        # number가 해당 횟수의 결과물을 담은 dp 배열에 들어가면 횟수 반환
        # 횟수가 1부터 시작하기 때문에 최솟값이 보장됨
        if number in dp[i]:
            return i
    return -1        