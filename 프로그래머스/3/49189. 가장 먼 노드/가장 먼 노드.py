from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    queue = deque()
    queue.append(1)
    visited[1] = 1
    while queue:
        node = queue.popleft()
        for n in graph[node]:
            if visited[n] == 0:
                visited[n] = visited[node] + 1
                queue.append(n)
    max_distance = max(visited)
    for r in visited[1:]:
        if r == max_distance:
            answer += 1
    return answer