from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n + 1)]
    
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
        
    distance = [-1] * (n + 1)

    queue = deque()
    queue.append([destination, 0])
    visited = set()
    while queue:
        v, l = queue.popleft()
        if v in visited:
            continue
        visited.add(v)
        distance[v] = l
        for i in graph[v]:
            queue.append([i, l + 1])
        
    for s in sources:
        answer.append(distance[s])
    
    return answer