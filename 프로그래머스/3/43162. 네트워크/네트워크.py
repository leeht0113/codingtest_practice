def dfs(i, visited, computers):
    visited[i] = 1
    for j in range(len(computers[0])):
        if computers[i][j] == 1 and visited[j] == 0:
            dfs(j, visited, computers)
    
def solution(n, computers):
    answer = 0
    visited = [0] * n
    for i in range(n):
        if visited[i] == 0:
            dfs(i, visited, computers)
            answer += 1
    return answer