from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n + 1)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    queue = deque([1])
    while queue:
        prev = queue.popleft()
        for n in graph[prev]:
            if visited[n] == 0:
                visited[n] = visited[prev] + 1
                queue.append(n)
    max_distance = max(visited[2:])
    for i in visited[2:]:
        if i == max_distance:
            answer += 1
    return answer