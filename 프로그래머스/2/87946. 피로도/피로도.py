def dfs(k, cnt, dungeons, visited):
    answer = cnt
    if answer == len(dungeons):
        return answer
    for i in range(len(dungeons)):
        if k >= dungeons[i][0] and visited[i] == 0:
            visited[i] = 1
            answer = max(answer, dfs(k - dungeons[i][1], cnt + 1, dungeons, visited))
            visited[i] = 0
    return answer

def solution(k, dungeons):
    n = len(dungeons)
    return dfs(k, 0, dungeons, [0] * n)