from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n + 1)]
    
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
        
    distance = [-1] * (n + 1)
    distance[destination] = 0
    queue = deque()
    queue.append([destination, 0])
    while queue:
        v, l = queue.popleft()
        for i in graph[v]:
            if distance[i] == -1:
                queue.append([i, l + 1])
                distance[i] = l + 1
    for s in sources:
        answer.append(distance[s])
    
    return answer