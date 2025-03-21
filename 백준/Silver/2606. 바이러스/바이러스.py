from collections import deque

computers = int(input())
pairs = int(input())

graph = [[] for _ in range(computers + 1)]
for _ in range(pairs):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (computers + 1)
queue = deque()
queue.append(1)
visited[1] = 1
while queue:
    c = queue.popleft()
    for i in graph[c]:
        if visited[i] == 0:
            queue.append(i)
            visited[i] = 1
print(sum(visited[2:]))