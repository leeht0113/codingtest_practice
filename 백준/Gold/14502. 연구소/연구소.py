from collections import deque
from itertools import product, combinations
from copy import deepcopy

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
x = list(range(0, n))
y = list(range(0, m))
prod = list(product(x, y))
combination = list(combinations(prod, 3))

virus = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            virus.append((i, j))

def bfs(graph, virus):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0 ,0]
    queue = deque(virus)
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            new_x = a + dx[i]
            new_y = b + dy[i]
            if 0 <= new_x < len(graph) and 0 <= new_y < len(graph[0]):
                if graph[new_x][new_y] == 0:
                    graph[new_x][new_y] = 2
                    queue.append((new_x, new_y))
    return graph

total_wall = []

for comb in combination:
    wall = []
    for c in comb:
        a, b = c
        if graph[a][b] == 0:
            wall.append((a, b))
    if len(wall) == 3:
        total_wall.append(wall)

answer = 0
for i in range(len(total_wall)):
    temp_graph = deepcopy(graph)
    for wall in total_wall[i]:
        a, b = wall
        temp_graph[a][b] = 1
    temp_graph = bfs(temp_graph, virus)
    temp = 0
    for i in range(len(temp_graph)):
        for j in range(len(temp_graph[1])):
            if temp_graph[i][j] == 0:
                temp += 1
    answer = max(answer, temp)

print(answer)