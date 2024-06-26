from collections import deque
import sys
input = sys.stdin.readline
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
visited = [-1] * (n + 1)
visited[x] = 0
queue = deque()
queue.append(x)
while queue:
    now = queue.popleft()
    for i in graph[now]:
        if visited[i] == -1:
            visited[i] = visited[now] + 1
            queue.append(i)
flag = 0
for i in range(1, n + 1):
    if visited[i] == k:
        print(i)
        flag = 1
if flag == 0:
    print(-1)