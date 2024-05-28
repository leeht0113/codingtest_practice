import heapq

def dijkstra(start, distance, graph):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance
    
    
def solution(N, road, K):
    answer = 0
    INF = int(1e9)
    graph = [[] for i in range(N + 1)]
    distance = [INF] * (N + 1)
    
    for r in range(len(road)):
        a, b, c = road[r]
        # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    distance = dijkstra(1, distance, graph)
    
    for i in range(1, len(distance)):
        if distance[i] <= K:
            answer += 1
    return answer