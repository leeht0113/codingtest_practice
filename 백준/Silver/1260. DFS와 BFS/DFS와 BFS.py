from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for g in graph:
    g.sort()
visited = [0] * (n + 1)
def dfs(answer, graph, start, visited):
    answer.append(start)
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            dfs(answer, graph, i, visited)
    return answer
answer = []
answer.append(dfs([], graph, v, visited))
def bfs(answer, graph, start):
    visited = [0] * (n + 1)
    visited[start] = 1
    queue = deque([start])
    answer.append(start)
    while queue:
        s = queue.popleft()
        for g in graph[s]:
            if visited[g] == 0:
                visited[g] = 1
                queue.append(g)
                answer.append(g)
    return answer
answer.append(bfs([], graph, v))
for a in answer:
    for i in a:
        print(i, end = ' ')
    print()