def dfs(cur_k, cnt, dungeons, visited):
    answer_max = cnt
    for idx, d in enumerate(dungeons):
        if cur_k >= d[0] and visited[idx] == 0:
            visited[idx] = 1
            answer_max = max(answer_max, dfs(cur_k - d[1], cnt + 1, dungeons, visited))
            visited[idx] = 0
    return answer_max

def solution(k, dungeons):
    visited = [0] * len(dungeons)
    answer_max = dfs(k, 0, dungeons, visited)
    return answer_max