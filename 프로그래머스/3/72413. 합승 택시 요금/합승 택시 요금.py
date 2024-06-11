import heapq

def solution(n, s, a, b, fares):
    answer = 0
    INF = float('inf')
    graph = [[] for i in range(n + 1)]
    
    for c, d, f in fares:
        graph[c].append((d, f))
        graph[d].append((c, f))
    
    def dijkstra(start):
        q = [(0, start)]
        distance = [INF] * (n + 1)
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
    
    min_distance = [dijkstra(i) for i in range(n + 1)]
    answer = INF
    for i in range(1, n + 1):
        answer = min(answer, min_distance[s][i] + min_distance[i][a] + min_distance[i][b])
    return answer