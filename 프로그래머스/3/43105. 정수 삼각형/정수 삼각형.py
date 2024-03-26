# 위에서 아래로 계산
def solution(triangle):
    n = len(triangle)
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = triangle[0][0]
    for i in range(1, n):
        for j in range(i + 1):
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
    return max(dp[-1])

# 아래서 위로 계산
# def solution(triangle):
#     answer = 0
#     n = len(triangle)
#     dp = [[0] * n for _ in range(n)]
#     for i in range(n):
#         dp[n-1][i] = triangle[n-1][i]
#     for i in range(n - 2, -1, -1):
#         for j in range(i + 1):
#             dp[i][j] = max(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]
#     return dp[0][0]