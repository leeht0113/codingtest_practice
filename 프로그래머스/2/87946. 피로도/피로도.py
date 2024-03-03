def dfs(cur_k, cnt, dungeons, visited):
    max_cnt = cnt
    for idx, d in enumerate(dungeons):
        if cur_k >= d[0] and visited[idx] == 0:
            visited[idx] = 1
            max_cnt = max(max_cnt, dfs(cur_k - d[1], cnt + 1, dungeons, visited))
            visited[idx] = 0
    return max_cnt

def solution(k, dungeons):
    return dfs(k, 0, dungeons, [0] * len(dungeons))