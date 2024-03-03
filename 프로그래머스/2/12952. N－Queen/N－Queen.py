def getAns(n, y, width, diagonal1, diagonal2):
    ans = 0
    if y == n:
        ans += 1
    else:
        for i in range(n): # 특정 행의 모든 열에 퀸을 놓아봄
            if width[i] or diagonal1[i + y] or diagonal2[i - y + n]:
                continue
            width[i] = diagonal1[i + y] = diagonal2[i - y + n] = True
            ans += getAns(n, y + 1, width, diagonal1, diagonal2)
            width[i] = diagonal1[i + y] = diagonal2[i - y + n] = False
    return ans

def solution(n):
    # y 값은 현재 위치가 결정된 퀸의 개수를 의미
    answer = getAns(n, 0, [False] * n, [False] * (n * 2), [False] * (n * 2))
    return answer