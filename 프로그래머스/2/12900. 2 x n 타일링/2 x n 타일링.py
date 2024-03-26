def solution(n):
    dp = [0] * n
    if n == 0:
        return 1
    if n == 1:
        return 2
    dp[0] = 1
    dp[1] = 2
    for i in range(2, n):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007
    return dp[n - 1] 